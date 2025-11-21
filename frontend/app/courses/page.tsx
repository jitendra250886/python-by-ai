import Link from "next/link";
import { API_BASE, fetchCourses, createCheckoutSession } from "../lib/api";

async function getCourses() {
  try {
    return await fetchCourses();
  } catch {
    return [];
  }
}

export default async function CoursesPage() {
  const courses: any[] = await getCourses();

  async function handleBuy(courseId: number) {
    "use server";
    const { checkout_url } = await createCheckoutSession(courseId);
    // In Next.js, you would typically redirect on the client, but for
    // simplicity we return the URL to be used in a link/button.
    return checkout_url as string;
  }

  return (
    <main className="min-h-screen bg-zinc-50 dark:bg-black p-8">
      <h1 className="mb-6 text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
        Courses
      </h1>
      {courses.length === 0 ? (
        <p className="text-zinc-700 dark:text-zinc-300">
          No courses available yet. Add some via the Django admin.
        </p>
      ) : (
        <ul className="space-y-4">
          {courses.map((course) => (
            <li
              key={course.id}
              className="rounded border border-zinc-200 bg-white p-4 shadow-sm dark:border-zinc-800 dark:bg-zinc-900"
            >
              <h2 className="text-lg font-medium text-zinc-900 dark:text-zinc-50">
                {course.title}
              </h2>
              <p className="text-sm text-zinc-700 dark:text-zinc-300">
                {course.short_description}
              </p>
              <p className="mt-1 text-sm font-semibold text-zinc-900 dark:text-zinc-100">
                Price: ${" "}
                {Number(course.price).toFixed(2)}
              </p>
              <div className="mt-3 flex items-center gap-3">
                <Link
                  href={`${API_BASE}/api/courses/${course.id}/`}
                  className="text-sm text-blue-600 hover:underline"
                >
                  View API JSON
                </Link>
                <form action={handleBuy.bind(null, course.id)}>
                  <button
                    type="submit"
                    className="rounded bg-black px-3 py-1.5 text-xs font-medium text-white hover:bg-zinc-800"
                  >
                    Buy (redirect to checkout)
                  </button>
                </form>
              </div>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}