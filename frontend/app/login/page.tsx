"use client";

import { FormEvent, useState } from "react";
import { login } from "../lib/api";

export default function LoginPage() {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setMessage(null);
    try {
      await login(identifier, password);
      setMessage("Logged in successfully. You can now access your courses.");
    } catch (err: any) {
      setMessage(err.message ?? "Login failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-zinc-50 dark:bg-black">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-sm space-y-4 rounded-lg bg-white p-6 shadow dark:bg-zinc-900"
      >
        <h1 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50">
          Login
        </h1>
        <label className="block text-sm text-zinc-700 dark:text-zinc-300">
          Username or Email
          <input
            className="mt-1 w-full rounded border px-3 py-2 text-sm dark:bg-zinc-800 dark:border-zinc-700"
            value={identifier}
            onChange={(e) => setIdentifier(e.target.value)}
          />
        </label>
        <label className="block text-sm text-zinc-700 dark:text-zinc-300">
          Password
          <input
            type="password"
            className="mt-1 w-full rounded border px-3 py-2 text-sm dark:bg-zinc-800 dark:border-zinc-700"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded bg-black px-3 py-2 text-sm font-medium text-white hover:bg-zinc-800 disabled:opacity-60"
        >
          {loading ? "Logging in..." : "Login"}
        </button>
        {message && (
          <p className="text-sm text-zinc-700 dark:text-zinc-300">{message}</p>
        )}
      </form>
    </main>
  );
}