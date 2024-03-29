from random import randint
from datetime import date, timedelta
from django.utils import timezone
from django.db.models import Q
from accounts.models import User, Roles, VerificationStatus
from trs.models import Room, Semester, TimeSlot, Semseters, Days_Of_Week
from courses.models import (
    CourseTitle,
    Course,
    CourseTime,
    MemberShip,
    MemberShipRoles,
    Session,
)
from assignments.models import (
    Assignment,
    FTQuestion as AssignmentFTQuestion,
    FTQuestionAnswer as AssignmentFTQuestionAnswer,
    MemberTakeAssignment,
    MemberAssignmentFTQuestion,
)
from exams.models import (
    Exam,
    FTQuestion as ExamFTQuestion,
    FTQuestionAnswer as ExamFTQuestionAnswer,
    MemberTakeExam,
    MemberExamFTQuestion,
)
from teachers.models import Teacher
from students.models import Student


def run():
    superuser = User.objects.create_superuser(
        "admin",
        email="admin@admin.admin",
        password="Abcd_1234",
        first_name="admin",
        last_name="espahbodi",
        phone_number="+989013971301",
    )
    print(f"superuser {superuser} created!\n\n")
    superuser.role = Roles.TEACHER * superuser.role
    superuser.save()
    users: list[User] = [
        User.objects.create_user(
            f"teacher{i}" if i < 3 else f"student{i-3}",
            email=f"teacher{i}@teacher.teacher"
            if i < 3
            else f"student{i-3}@student.student",
            password=f"Abcd_1234",
            first_name=f"teacher{i}" if i < 3 else f"student{i-3}",
            last_name=f"teacher" if i < 3 else f"student",
            phone_number=f"+98901397140{i}" if i < 3 else f"+98901397150{i-3}",
            role=Roles.NOT_DEFINED,
            verification_status=VerificationStatus.BOTH,
        )
        for i in range(10)
    ]
    print(f"users {users} created!\n\n")

    student: list[Student] = [
        Student.objects.create(user=users[i], school="some", degree=1, field="some")
        for i in range(3, 10)
    ]
    print(f"student {student} created!\n\n")

    teachers: list[Teacher] = [
        Teacher.objects.create(user=users[i], experience=30) for i in range(3)
    ]
    print(f"teachers {teachers} created!\n\n")

    rooms: list[Room] = [
        Room.objects.create(room_title="room 1", capacity=45),
        Room.objects.create(room_title="room 2", capacity=50),
    ]
    print(f"rooms {rooms} created!\n\n")

    semesters: list[Semester] = [
        Semester.objects.create(year="1402-1403", semester=Semseters.FIRST_SEMESTER),
        Semester.objects.create(year="1402-1403", semester=Semseters.SECOND_SEMESTER),
    ]
    print(f"semesters {semesters} created!\n\n")

    times = [
        {"start": "08:00:00", "end": "09:30:00"},
        {"start": "10:00:00", "end": "11:30:00"},
        {"start": "14:00:00", "end": "15:30:00"},
    ]
    timeslots: list[TimeSlot] = [
        TimeSlot.objects.create(
            room_number=rooms[i], day=day_of_week, start=time["start"], end=time["end"]
        )
        for time in times
        for i in range(0, 2)
        for day_of_week in [
            Days_Of_Week.MONDAY,
            Days_Of_Week.THURSDAY,
            Days_Of_Week.TUESDAY,
            Days_Of_Week.SUNDAY,
        ]
    ]
    print(f"timeslots {timeslots} created!\n\n")

    coursetitles: list[CourseTitle] = [
        CourseTitle.objects.create(title="math"),
        CourseTitle.objects.create(title="physic"),
        CourseTitle.objects.create(title="algebra"),
    ]
    print(f"coursetitles {coursetitles} created!\n\n")

    courses: list[Course] = [
        Course.objects.create(
            course_number=j,
            course_title=coursetitles[i],
            semester=semesters[0],
            start_date=date.today(),
            end_date=(timezone.now() + timedelta(weeks=12)).date(),
            tuition=10000000,
            tuition_percentage=27.5,
        )
        for j in range(1, 4)
        for i in range(0, 3)
    ]
    print(f"courses {courses} created!\n\n")

    student_membership: list[MemberShip] = [
        MemberShip.objects.create(
            user=student[j].user, course=courses[i], role=MemberShipRoles.STUDENT
        )
        for j in range(0, len(student))
        for i in range(0, len(courses))
        if (i + j < len(student))
    ]
    print(f"student_membership {student_membership} created!\n\n")

    teacher_membership: list[MemberShip] = [
        MemberShip.objects.create(
            user=teachers[i].user, course=courses[i], role=MemberShipRoles.TEACHER
        )
        for i in range(min(len(teachers), len(courses)))
    ]
    print(f"student_membership {teacher_membership} created!\n\n")

    course_time: list[CourseTime] = [
        CourseTime.objects.create(
            course=courses[index % len(courses)],
            semester=courses[index % len(courses)].semester,
            time_slot=timeslots[index],
        )
        for index in range(len(timeslots))
    ]
    print(f"course_time {course_time} created!\n\n")
    sessions = Session.objects.filter(
        Q(session_number=0) | Q(session_number=1) | Q(session_number=2)
    ).all()
    current_time = timezone.now()
    two_week_later = current_time + timedelta(weeks=2)
    for session in sessions:
        exam = Exam.objects.create(
            session=session,
            title="exam",
            description=f"simple exam for {session}",
            exam_number=0,
            start_at=current_time,
            end_at=two_week_later,
        )
        exam_questions = []
        for i in range(randint(3, 5)):
            exam_questions.append(
                ExamFTQuestion(
                    exam=exam,
                    title="simple question",
                    text=f"simple question {i} for exam {exam}",
                    start_at=current_time,
                    end_at=two_week_later,
                )
            )
        exam_questions = ExamFTQuestion.objects.bulk_create(exam_questions)
        exam_question_answers = []
        for exam_question in exam_questions:
            exam_question_answers.append(
                ExamFTQuestionAnswer(
                    ft_question=exam_question,
                    answer_text=f"simple answer for {exam_question}",
                    accessing_at=two_week_later,
                )
            )
        ExamFTQuestionAnswer.objects.bulk_create(exam_question_answers)
        assignment = Assignment.objects.create(
            session=session,
            title="assignment",
            description=f"simple assignment for {session}",
            assignment_number=0,
            start_at=current_time,
            end_at=two_week_later,
        )
        assignment_questions = []
        for i in range(randint(3, 5)):
            assignment_questions.append(
                AssignmentFTQuestion(
                    assignment=assignment,
                    title="simple question",
                    text=f"simple question {i} for assignment {assignment}",
                    start_at=current_time,
                    end_at=two_week_later,
                )
            )
        assignment_questions = AssignmentFTQuestion.objects.bulk_create(
            assignment_questions
        )
        assignment_question_answers = []
        for assignment_question in assignment_questions:
            assignment_question_answers.append(
                AssignmentFTQuestionAnswer(
                    ft_question=assignment_question,
                    answer_text=f"simple answer for {assignment_question}",
                    accessing_at=two_week_later,
                )
            )
        AssignmentFTQuestionAnswer.objects.bulk_create(assignment_question_answers)
    print(f"for sessions {sessions} exam ans assignment created")

    # create SOME MEMBER ANSWER for assignment with id 11 ans ftquestion with id 42 ans exam with 11 11 and exam ftquestion with id 38
    # for student0
    asnwers = [
        {"student": "student0", "answer": "Reading is a great way to relax."},
        {"student": "student1", "answer": "I love to read books."},
        {"student": "student2", "answer": "Programming is my passion."},
        {"student": "student3", "answer": "Traveling broadens the mind."},
        {"student": "student4", "answer": "Music is the universal language."},
        {"student": "student5", "answer": "programming is my favorite job"},
    ]

    print("create member answer for assignment 11 and first ftquestion")

    assignment = Assignment.objects.get(id=11)
    assignment_ftquestion = AssignmentFTQuestion.objects.filter(
        assignment=assignment
    ).first()

    for answer in asnwers:
        pass
        member = MemberShip.objects.get(user__username=answer["student"], course_id=1)
        member_take_assignemnt = MemberTakeAssignment.objects.create(
            assignment=assignment,
            member=member,
            last_visit=timezone.now(),
            finish_at=timezone.now(),
            score=None,
        )
        MemberAssignmentFTQuestion.objects.create(
            member_take_assignment=member_take_assignemnt,
            ft_question=assignment_ftquestion,
            answered_text=answer["answer"],
            answered_file=None,
            score=None,
        )
    print("member answer for assignment 11 and first ftquestion created")

    print("create member answer for assignment 11 and first ftquestion")

    exam = Exam.objects.get(id=11)
    exam_ftquestion = ExamFTQuestion.objects.filter(exam=exam).first()

    for answer in asnwers:
        pass
        member = MemberShip.objects.get(user__username=answer["student"], course_id=1)
        member_take_assignemnt = MemberTakeExam.objects.create(
            exam=exam,
            member=member,
            last_visit=timezone.now(),
            finish_at=timezone.now(),
            score=None,
        )
        MemberExamFTQuestion.objects.create(
            member_take_exam=member_take_assignemnt,
            ft_question=exam_ftquestion,
            answered_text=answer["answer"],
            answered_file=None,
            score=None,
        )
    print("member answer for exam 11 and first ftquestion created")
