export const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

async function apiFetch(path: string, options: RequestInit = {}) {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, {
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API error ${res.status}: ${text}`);
  }

  return res.json();
}

export async function login(identifier: string, password: string) {
  return apiFetch("/api/auth/login/", {
    method: "POST",
    body: JSON.stringify({ username: identifier, password }),
  });
}

export async function register(username: string, email: string, password: string) {
  return apiFetch("/api/auth/register/", {
    method: "POST",
    body: JSON.stringify({ username, email, password }),
  });
}

export async function logout() {
  return apiFetch("/api/auth/logout/", { method: "POST" });
}

export async function fetchMe() {
  return apiFetch("/api/auth/me/");
}

export async function fetchCourses() {
  return apiFetch("/api/courses/");
}

export async function createCheckoutSession(courseId: number) {
  return apiFetch("/api/orders/create-checkout-session/", {
    method: "POST",
    body: JSON.stringify({ course_id: courseId }),
  });
}

export async function fetchEnrollments() {
  return apiFetch("/api/enrollments/");
}