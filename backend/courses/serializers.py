from rest_framework import serializers

from .models import Course, Lesson, Enrollment, LessonProgress, Order


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "course",
            "title",
            "order",
            "content_path",
            "is_preview",
            "created_at",
            "updated_at",
        ]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "full_description",
            "price",
            "is_published",
            "created_at",
            "updated_at",
            "lessons",
        ]


class CourseSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "slug",
            "price",
        ]


class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = [
            "id",
            "lesson",
            "is_completed",
            "completed_at",
            "last_viewed_at",
        ]


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSummarySerializer(read_only=True)
    progress_percent = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "course",
            "status",
            "source",
            "started_at",
            "expires_at",
            "created_at",
            "updated_at",
            "progress_percent",
        ]

    def get_progress_percent(self, obj: Enrollment) -> float:
        total_lessons = obj.course.lessons.count()
        if total_lessons == 0:
            return 0.0
        completed = obj.lesson_progress.filter(is_completed=True).count()
        return round((completed / total_lessons) * 100, 2)


class EnrollmentDetailSerializer(EnrollmentSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta(EnrollmentSerializer.Meta):
        fields = EnrollmentSerializer.Meta.fields + ["lessons"]

    def get_lessons(self, obj: Enrollment):
        """Return lessons with completion status for this enrollment."""

        lessons = obj.course.lessons.order_by("order")
        progress_by_lesson = {
            lp.lesson_id: lp
            for lp in obj.lesson_progress.select_related("lesson")
        }
        data = []
        for lesson in lessons:
            lp = progress_by_lesson.get(lesson.id)
            data.append(
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "order": lesson.order,
                    "is_completed": bool(lp and lp.is_completed),
                }
            )
        return data


class OrderSerializer(serializers.ModelSerializer):
    course = CourseSummarySerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "course",
            "amount",
            "currency",
            "status",
            "provider",
            "created_at",
            "updated_at",
        ]
