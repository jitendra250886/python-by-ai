# End-to-End Deployment Guide

This guide explains **every step** needed to go from a fresh project to a live, revenue-generating website:

1. Choosing and purchasing hosting
2. Preparing the server
3. Deploying the Django backend
4. Deploying the Next.js frontend
5. Configuring the domain and HTTPS
6. Launch checklist

It assumes you are deploying to a single Linux VPS (e.g., DigitalOcean Droplet, AWS Lightsail, Linode, etc.).

> Names of providers are examples. You can use any VPS provider as long as you can SSH into the server and install software.

---

## 1. Choose and Purchase Hosting

### 1.1 What You Need

For an MVP with a few hundred users, a small VPS is enough:

- 2 vCPUs
- 4 GB RAM
- 80+ GB SSD
- Ubuntu 22.04 LTS (or similar Linux distribution)

### 1.2 Steps to Purchase Hosting (Example Flow)

1. Create an account with a VPS provider.
2. Create a new server (droplet/instance):
   - OS: Ubuntu 22.04 LTS (recommended)
   - Plan: "basic" with 2 vCPUs / 4GB RAM or similar
   - Region: choose a region close to most users
3. Add SSH keys or set a strong root password.
4. Once created, note the server’s **public IP address**.

---

## 2. Prepare the Server

SSH into your server from your local machine:

```bash
ssh root@YOUR_SERVER_IP
```

Replace `YOUR_SERVER_IP` with the actual IP address.

### 2.1 Create a Non-Root User

```bash
adduser deploy
usermod -aG sudo deploy
su - deploy
```

From now on, run commands as the `deploy` user.

### 2.2 Install System Packages

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git nginx postgresql postgresql-contrib nodejs npm
```

This installs:

- Python 3 + `venv` and `pip` for Django backend
- Git to pull your repository
- Nginx as the web server / reverse proxy
- PostgreSQL as the production database
- Node.js + npm for the Next.js frontend

### 2.3 Configure PostgreSQL

```bash
sudo -u postgres psql
```

In the PostgreSQL shell:

```sql
CREATE DATABASE python_master_course;
CREATE USER python_user WITH PASSWORD 'STRONG_PASSWORD_HERE';
ALTER ROLE python_user SET client_encoding TO 'utf8';
ALTER ROLE python_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE python_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE python_master_course TO python_user;
\q
```

Record the database name, user, and password; you will use them in Django settings.

---

## 3. Deploy the Django Backend

### 3.1 Clone the Repository

From the `deploy` user’s home directory:

```bash
cd ~
mkdir apps
cd apps
git clone YOUR_REPO_URL python-master-course
cd python-master-course
```

Replace `YOUR_REPO_URL` with your Git repository URL.

### 3.2 Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install "django>=5,<6" djangorestframework psycopg2-binary gunicorn
```

`gunicorn` will serve the Django app behind Nginx.

### 3.3 Configure Django for Production

Edit `backend/core/settings.py` for production use:

- Set `DEBUG = False`.
- Set `ALLOWED_HOSTS = ["your-domain.com", "YOUR_SERVER_IP"]`.
- Configure the `DATABASES` setting to use PostgreSQL:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "python_master_course",
        "USER": "python_user",
        "PASSWORD": "STRONG_PASSWORD_HERE",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

> For a more flexible setup, you can move these values to environment variables and read them in `settings.py`.

### 3.4 Apply Migrations and Create Superuser

```bash
cd ~/apps/python-master-course
source .venv/bin/activate
python backend/manage.py migrate
python backend/manage.py createsuperuser
```

### 3.5 Collect Static Files (Optional for Now)

Later, when you add admin styles and static assets, you will run:

```bash
python backend/manage.py collectstatic
```

This gathers static files into one directory for Nginx to serve.

### 3.6 Configure Gunicorn Service

Create a systemd service file, e.g., `/etc/systemd/system/python-backend.service`:

```ini
[Unit]
Description=Gunicorn daemon for Python Master Course backend
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/home/deploy/apps/python-master-course
Environment="PATH=/home/deploy/apps/python-master-course/.venv/bin"
ExecStart=/home/deploy/apps/python-master-course/.venv/bin/gunicorn core.wsgi:application \
    --chdir backend \
    --bind 127.0.0.1:8001 \
    --workers 3

[Install]
WantedBy=multi-user.target
```

Then enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable python-backend
sudo systemctl start python-backend
sudo systemctl status python-backend
```

If everything is configured correctly, the backend should now be running on `127.0.0.1:8001`.

---

## 4. Deploy the Next.js Frontend

### 4.1 Build the Frontend

Once the `frontend/` app is created and committed, on the server:

```bash
cd ~/apps/python-master-course/frontend
npm install
npm run build
```

### 4.2 Start the Frontend (Simple Approach)

For an MVP, you can run the Next.js production server behind Nginx:

```bash
npm run start -- -p 3000
```

To run this as a service, create `/etc/systemd/system/python-frontend.service`:

```ini
[Unit]
Description=Next.js app for Python Master Course
After=network.target

[Service]
User=deploy
WorkingDirectory=/home/deploy/apps/python-master-course/frontend
Environment="NODE_ENV=production"
ExecStart=/usr/bin/npm run start -- -p 3000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable python-frontend
sudo systemctl start python-frontend
sudo systemctl status python-frontend
```

The frontend should now be running on `127.0.0.1:3000`.

---

## 5. Configure Nginx, Domain, and HTTPS

### 5.1 Point Your Domain to the Server

In your domain registrar’s dashboard:

1. Create an `A` record:
   - Name: `@` (or `www`, depending on your setup)
   - Value: `YOUR_SERVER_IP`
2. Wait for DNS propagation (can take from minutes up to 24 hours).

### 5.2 Configure Nginx as a Reverse Proxy

Create an Nginx server block, e.g., `/etc/nginx/sites-available/python-master-course`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location /api/ {
        proxy_pass http://127.0.0.1:8001/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        proxy_pass http://127.0.0.1:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the config and test Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/python-master-course /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Now visiting `http://your-domain.com` should show your Next.js frontend, and `/api/` routes should reach Django.

### 5.3 Enable HTTPS with Let's Encrypt (Certbot)

Install Certbot:

```bash
sudo apt install -y certbot python3-certbot-nginx
```

Run Certbot:

```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

Follow the prompts to obtain and install SSL certificates. Certbot will update your Nginx config to redirect HTTP to HTTPS.

---

## 6. Launch Checklist

Before announcing the site publicly, verify:

- [ ] Backend API responds correctly at `https://your-domain.com/api/courses/`
- [ ] Admin login works at `https://your-domain.com/admin/`
- [ ] Frontend loads at `https://your-domain.com/`
- [ ] Basic navigation (home → courses → course detail) works
- [ ] Any environment variables (Stripe keys, email settings, etc.) are configured
- [ ] `DEBUG = False` in Django settings
- [ ] Regular backups configured for the database

As you add payments, live classes, and more advanced features, this guide can be extended with:

- Stripe configuration and webhooks
- Email sending setup (e.g., SendGrid)
- Logging and monitoring (e.g., Sentry, system journal)

For now, this gives you a **complete, end-to-end path** from a fresh server to a live platform running the Python Master Course backend and frontend.
