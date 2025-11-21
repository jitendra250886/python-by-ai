import Image from "next/image";

import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-zinc-50 dark:bg-black">
      <div className="w-full max-w-xl rounded-lg bg-white p-8 shadow dark:bg-zinc-900">
        <h1 className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
          Python Master Course Platform
        </h1>
        <p className="mt-2 text-sm text-zinc-700 dark:text-zinc-300">
          This is the frontend for your Django-powered course platform.
        </p>
        <div className="mt-6 flex flex-col gap-3">
          <Link
            href="/login"
            className="rounded bg-black px-4 py-2 text-sm font-medium text-white hover:bg-zinc-800"
          >
            Login
          </Link>
          <Link
            href="/courses"
            className="rounded border border-zinc-200 px-4 py-2 text-sm font-medium text-zinc-900 hover:bg-zinc-100 dark:border-zinc-700 dark:text-zinc-50 dark:hover:bg-zinc-800"
          >
            View Courses
          </Link>
        </div>
      </div>
    </main>
  );
}
