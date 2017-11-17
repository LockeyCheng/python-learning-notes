# -*- coding: UTF-8 -*-
'''
Created on 2017年9月3日
Running environment：win7.x86_64 eclipse python3
author: Lockey
email:lockey@123.com
desc:
'''

import time
import datetime

#定义一个学校类包含私有属性以及成员方法
class School(object):
    'This is class for School model'
    __admins = {}
    __teachers = {}
    __students = {}
    __courses = {}
    #初始化类
    def __init__(self):
        pass
    #激活、真正创建一个学校实例
    def schoolactivate(self,school_name,school_location,school_motto):
        self.__school_name = school_name
        self.__school_location = school_location
        self.__school_motto = school_motto
    #添加系统管理员
    def adminAdd(self,adminname,obj):
        self.__admins.setdefault(adminname,obj)
        return True
    #获得系统管理员信息
    def getAdmins(self):
        return self.__admins
    #获取学校成员如老师和学生的信息
    def getUser(self,usertype):
        if usertype == 'teacher':
            return self.__teachers
        elif usertype == 'student':
            return self.__students
        else:
            return False
    #添加课程
    def addCourse(self):
        courses = self.getCourses()
        totalCourses = len(courses)
        cname = ''; cprice = ''; ctime = ''
        try:
            while True:
                if cname == '':
                    cname = input('Please input your course name : ')
                    if cname in courses:
                        cname = ''
                        print('Courses already exists!')
                        return
                    if cname == '':
                        print('course name can not be blank, please reinput!')
                        continue

                if cprice == '':
                    cprice = input('Please input your course price : ')
                    if cprice == '':
                        print('course price can not be blank, please reinput!')
                        continue
                    try:
                        if 0> int(cprice) >100000:
                            print('Illegal price value, too high price againsts the law!')
                            cprice = ''
                            continue
                    except:
                        cprice = ''
                        print('Illegal price value, number is required!')
                        continue
                if ctime == '':
                    ctime = input('Please input your course time (eg:2017-09-03): ')
                    if ctime == '':
                        print('course time can not be blank, please reinput!')
                        continue
                    if ctime.count('-') != 2:
                        print('Time format illegal!')
                        ctime = ''
                        continue
                    if not valid_date(ctime):
                        print('Time format illegal!')
                        ctime = ''
                        continue
                break
            cnumber = 'course'+str(totalCourses+1)
            #创建课程实例
            course = Course(cnumber,cname,cprice,ctime)
            self.__courses.setdefault(cname,course)
            self.__students.setdefault(cname)
            print('Course %s successfully added!'%cname)
            course.showInfo()
            return True
        except:
            return False
    #获取课程信息
    def getCourses(self):
        return self.__courses
    #招收学生
    def addStudent(self):
        courses = self.__courses
        students = self.__students
        sname = ''; sage = ''; sgender = ''; sclassof = ''
        while True:
            if sname == '':
                sname = input('Please input student name : ')
                if sname == '':
                    print('student name can not be blank, please reinput!')
                    continue

            if sclassof == '':
                sclassof = input('Please input student course : ')
                if sclassof not in courses:
                    courseLst = []
                    for item in courses:
                        courseLst.append(item)
                    print('No such course to attend, please input one of following items as your course!\n')
                    print(courseLst)
                    sclassof = ''
                    continue
            classStudents = self.__students[sclassof]
            if classStudents and sname in classStudents:
                print('Student {} already in class {}'.format(sname, sclassof))
                return False

            if sage == '':
                sage = input('Please input student age(6-120) : ')
                if sage == '':
                    print('student age can not be blank, please reinput!')
                    continue
                try:
                    age = int(sage)
                    if 0< age <=120:
                        pass
                    else:
                        sage = ''
                        print('Illegal human age, are your a neuropath!!')
                        continue
                except:
                    sage = ''
                    print('Illegal human age, number within 10000 is required!')
                    continue
            if sgender == '':
                sgender = input('Please input student gender (male|female): ')
                if sgender == '':
                    print('student gender can not be blank, please reinput!')
                    continue
                if sgender == 'male' or sgender == 'female':
                    continue
                else:
                    print('invalid gender!')
                    sgender = ''
                    continue

            break

        fees = - int(courses[sclassof].price)
        try:
            studentTotal = len(students[sclassof])
        except:
            studentTotal = 0
        finally:
            studentno = 'student'+sclassof+str(studentTotal+1)
                #创建学生实例
            student = Student(sname, 'student', sage, sgender, sclassof, studentno,fees)
            try:
                if len(self.__students[sclassof]):
                    self.__students[sclassof].setdefault(sname,student)
            except:
                self.__students[sclassof]={sname:student}
            print('Student %s successfully added, infos are as below:'%sname)
            course = courses[sclassof]
            student.showInfo(course)
            return True

    def deleteUser(self):
        while True:
            type = input('Please input user type [(a)dmin,(t)eacher,(s)tudent] (Q to quit): ')
            type=type.lower()
            if type == 'q':
                break
            if type not in 'ats':
                print('User type does not exist!')
                return

            if type == 'a':
                userDict = self.__admins
            elif type == 't':
                userDict = self.__teachers
            else:
                classof = input('Please input student class: ')
                if classof not in self.__courses:
                    print('No such class!')
                    continue
                userDict = self.__students[classof]
            username = input('Please input username to delete: ')
            if username in userDict:
                if username == 'admin':
                    print('Operation forbidden, super administrator can not be destroyed!')
                    continue
                if type == 'a' or type == 't':
                    del userDict[username]
                    print('User %s successfully deleted!'%username)
                    continue
                if userDict[username].feestate > 0:
                    refund = input('Current student has paid the fees, sure to refund and delete(Y/N): ')
                    if refund in 'nN':
                        print('Cancel deleting student %s'%username)
                        continue
                del userDict[username]
                print('Student %s successfully deleted!'%username)
                continue
            print('User %s does not exist!'%username)

    #招收讲师
    def addTeacher(self):
        teachers = self.getUser('teacher')
        tname=''; tage=''; tgender=''; tcourse=''; tsalary=''
        try:
            while True:
                    if tname == '':
                        tname = input('Please input teacher name : ')
                        if tname in teachers:
                            tname = ''
                            print('teacher already exists!')
                            return
                        if tname == '':
                            print('teacher name can not be blank, please reinput!')
                            continue

                    if tage == '':
                        tage = input('Please input teacher age(6-120) : ')
                        if tage == '':
                            print('teacher age can not be blank, please reinput!')
                            continue
                        try:
                            age = int(tage)
                            if 0< age <=120:
                                pass
                            else:
                                tage = ''
                                print('Illegal human age, are your a neuropath!!')
                                continue

                        except:
                            tage = ''
                            print('Illegal human age, number within 10000 is required!')
                            continue
                    if tgender == '':
                        tgender = input('Please input teacher gender (male|female) : ')
                        if tgender == '':
                            print('teacher gender can not be blank, please reinput!')
                            continue
                        if tgender == 'male' or tgender == 'female':
                            continue
                        else:
                            print('invalid gender!')
                            tgender = ''
                            continue
                    if tcourse == '':
                        courses = self.getCourses()
                        tcourse = input('Please input teacher course : ')
                        if tcourse == 'quit':
                            return
                        if tcourse not in courses:
                            courseLst = []
                            for item in courses:
                                courseLst.append(item)
                            print('No such course to attend, please input one of following items as your course!\n')
                            print(courseLst)
                            tcourse = ''
                            continue

                    if tsalary == '':
                        tsalary = input('Please input teacher salary : ')
                        if tsalary == '':
                            print('teacher salary can not be blank, please reinput!')
                            continue
                        try:
                            if int(tsalary):
                                pass
                        except:
                            print('Illegal salary value, number is required!')
                            tsalary = ''
                            continue
                    break
            totalteacher = len(teachers)
            teacherno = 'teacher'+str(totalteacher+1)
            #创建老师实例
            teacher = Teacher(tname, 'teacher',tage, tgender, tcourse, tsalary, teacherno)
            self.__teachers.setdefault(tname,teacher)
            print('Teacher %s successfully added, infos as below:'%tname)
            course = courses[tcourse]
            teacher.showInfo(course)
            return True
        except:
            return False
    #查看学校信息
    def getSchoolInfo(self):
        ret = (self.__school_name,self.__school_location,self.__school_motto)
        return ret
#定义课程类
class Course(object):
    def __init__(self,cnumber,cname,cprice,ctime):
        self.number = cnumber
        self.name = cname
        self.price = cprice
        self.time = ctime
    #定义课程显示的方法
    def showInfo(self):
        print("""
        Infomation for course {}

            number : {}
            name : {}
            price : {}
            time: {}
            """.format(self.name, self.number, self.name, self.price, self.time))
#定义学校成员类，作为老师和学生的基类
class Member(object):
    def __init__(self,name,password,age,gender,*arg):
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender

    def showInfo(self):
       pass
    def changePassword(self):
        orign = False
        while True:
            if orign == False:
                password = input('Please input old password to authenticate: ')
                if password != self.password:
                    print('Original password not correct, try again!')
                    continue
                orign = True
            password1 = input('Please input new password(Q to quit): ')
            if password1 in 'Qq':
                return False

            if password1 == self.password:
                print('Passwords can not be the same as the old one, try again!')
                continue

            if len(password1) < 6:
                print('Passwords must more than 5 characters , try again!')
                continue

            password2 = input('Please confirm password: ')
            if password1 != password2:
                print('Passwords not equal, try again!')
                continue
            self.password = password1
            print('Passwords successfully changed!')
            break
#定义老师类
class Teacher(Member):

    def __init__(self,name,password,age,gender,*arg):
        super().__init__(name,password,age,gender)
        self.course = arg[0]
        self.salary = arg[1]
        self.number = arg[2]

    def showInfo(self,obj):
        print("""
        Infomation for teacher {}

            number : {}
            name : {}
            age : {}
            gender: {}
            course : {}
                course number:{}
                course price :{}
                course time  :{}
            salary : {}
            """.format(self.name, self.number, self.name, self.age, self.gender, self.course, obj.number, obj.price, obj.time, self.salary))
    #老师讲课的方法函数
    def giveLecture(self):
        print('Course {} start ...'.format(self.course))
        for i in range(5,0,-1):
            time.sleep(1)
            print('Course {} will over after {} seconds...'.format(self.course,i))
            i = i - 1
        print('Course {} over ...'.format(self.course))
    #老师查看自己所带课程的学生信息
    def viewStudents(self,students):
                print("""
        Student attending {} are as below""".format(self.course))
                print("""
    number   name   age   gender   class""")
                for stu in students:
                    print('    {} {}      {}     {}        {}'.format(stu.number,stu.name,stu.age,stu.gender,stu.classof))
#定义学生类
class Student(Member):

    def __init__(self,name,password,age,gender,*arg):
        super().__init__(name,password,age,gender)
        self.classof = arg[0]
        self.number = arg[1]
        self.feestate = arg[2]
    #定义学生学习的方法
    def learning(self):
        print('{} start learning ...'.format(self.name))
        for i in range(5,0,-1):
            time.sleep(1)
            print('{} keep learning ...'.format(self.name))
            i = i - 1
        print('{} stop learning and go to date ...'.format(self.name))
    #定义学生缴费的方法函数
    def payFees(self):
        if self.feestate < 0:
            self.feestate *= -1
            print('Fees paid off!')
            return
        else:
            print('Fees already paid!')
            return

    def showInfo(self,obj):
        print("""
        Infomation for student {}

            number : {}
            name : {}
            age : {}
            gender : {}
            feeState : {}
            class : {}
                course number:{}
                course price :{}
                course time  :{}
            """.format(self.name, self.number, self.name, self.age, self.gender, self.feestate, self.classof,obj.number, obj.price, obj.time))
#用来判断输入的日期是否合规范
def valid_date(dateStr):
    try:
        year, month, day = map(int,dateStr.split('-'))
        mDay = [31,28,31,30,31,30,31,31,30,31,30,31]
        if 2017<=year<=2038 and 1<=month<=12 and 1<=day<=31:
            if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
                mDay[1] = 29
            if day > mDay[month-1] :
                return False
            return True
        return False
    except:
        return False
#判断当前时段，返回一个时间段的代表值作为问候语的一部分
def period():
    currentTime = datetime.datetime.now()
    hour = currentTime.hour
    if 6 <= hour < 12:
        return 'morning!'
    if 12 <= hour < 14:
        return 'midday!'
    if 14 <= hour < 18:
        return 'afternoon!'
    if 18 <= hour < 20:
        return 'evening!'
    else:
        return 'night'
#所有相关用户的登录函数，用来进行登录限制
def userloginCheck(usertype,obj):
    if usertype == 'admin':
        admins = obj.getAdmins()
        userDict = admins
    else:
        userDict = obj.getUser(usertype)
        if usertype == 'student':
            course = input('Please input your class: ')
            if course in userDict:
                userDict = userDict[course]
            else:
                print('No such class!')
                return False
    loginuser = False
    userAttempt = 0
    while userAttempt < 3:

        username = input('Please input username: ')
        userAttempt += 1
        if not userDict.get(username):
            print('Username not exist!')
            continue
        password = input('Please input password: ')
        if password == userDict[username].password:
            passwordCheck = checkPassword(usertype,userDict[username],password)
            if passwordCheck:
                loginuser = userDict[username]
            break
        else:
            print('Username or password not correct!')

    if userAttempt >= 3:
        print('User {} has tried 3 times, please login later!'.format(username))
    return loginuser
#用户初次登录强制修改密码函数
def checkPassword(usertype,obj,oldpwd):
    defaultPwd={'admin':'admin','teacher':'teacher','student':'student'}
    if defaultPwd[usertype] == oldpwd:
        print('For first logged in user, password should be changed!')
        while True:
            password1 = input('Please input new password: ')
            if password1 in 'Qq':
                return False

            if password1 == oldpwd:
                print('Passwords can not be the same as the old one, try again!')
                continue

            password2 = input('Please confirm password: ')
            if password1 != password2 and password1 != '':
                print('Passwords not equal, try again!')
                continue

            if len(password1) < 6:
                print('Passwords must more than 5 characters , try again!')
                continue

            obj.password = password1
            break
    return True
#管理员管理模块函数
def systemManage(user,school):
    greeting = period()
    oplist = """
    Good {} administator [ {} ]

            menu lists

        (M) : school manage
        (C) : course Eroll
        (T) : teacher Eroll
        (S) : student Eroll
        (VT) : view teachers
        (VS) : view students
        (VC) : view courses
        (P) : change password
        (A) : add administrator
        (D) : delete user(admin/teacher/student)
        (Q) : quit
            """.format(greeting, user.name)
    print(oplist)
    while True:
        userChoice = input('Please input your operation (o to  show menu): ')
        if userChoice in 'Mm':
            schoolInfo = school.getSchoolInfo()
             #学校信息管理
            print("""
    Information for school {}

          name: {}
          location: {}
          motto:{}
        """.format(schoolInfo[0],schoolInfo[0],schoolInfo[1],schoolInfo[2]))
            continue
        if userChoice in 'oO':
            print(oplist)
            continue
        if userChoice in 'Cc':
            result =  school.addCourse()
            if not result:
                print('Course adding failed!')
            continue

        elif userChoice in 'Tt':
            result = school.addTeacher()
            if not result:
                print('Teacher enrolling failed!')
            continue

        elif userChoice in 'Ss':
            result = school.addStudent()
            if not result:
                print('Student enrolling failed!')
            continue

        elif userChoice in 'VSvsVsvS':
            studentDict = school.getUser('student')
            if len(studentDict) > 0:
                try:
                    for course in studentDict:
                        if len(studentDict[course]) > 0:
                            print("""
            Students attending {} are as below""".format(course))
                            print("""
        number   name   age   gender   class""")
                            for student in studentDict[course]:
                                stu = studentDict[course][student]
                                print('       {} {}      {}     {}        {}'.format(stu.number,stu.name,stu.age,stu.gender,stu.classof))
                except:
                    print('\nNo students info to show!\n')
            else:
                print('\nNo students info to show!\n')
        elif userChoice in 'VTvtVtvT':
            teachers = school.getUser('teacher')
            try:
                if len(teachers) > 0:
                    print("""
                Teachers information are as below:

            number   name   age   gender   course   salary""")
                    for item in teachers:
                        teacher = teachers[item]
                        print('       {} {}      {}     {}        {}         {}'.format(teacher.number,teacher.name,teacher.age,teacher.gender,teacher.course,teacher.salary))
                else:
                    print('\nNo teachers info to show!\n')
            except:
                print('No teachers info to show!')
        elif userChoice in 'VCvcVcvC':
            courses = school.getCourses()
            if len(courses) > 0:
                print("""
            Courses information are as below:

        number   name   price   time""")
                for item in courses:
                    course = courses[item]
                    print('       {}  {}      {}      {}'.format(course.number,course.name,course.price,course.time))
            else:
                print('\nNo courses info to show!\n')
        elif userChoice in 'pP':
            user.changePassword()
            continue
        elif userChoice in 'aA':
            while True:
                    adminname = input('Please input administrator name(q to quit) : ')
                    if adminname in 'qQ':
                        break
                    if adminname in school.getAdmins():
                        print('Administrator %s already exists!'%adminname)
                        continue
                    admin = Member(adminname,'admin','admin','admin')
                    result = school.adminAdd(adminname, admin)
                    if result:
                        print('Administrator successfully added with default password "admin"! ')
                        break
                    print('Failed to add administrator %s!'%adminname)
            continue
        elif userChoice in 'dD':
            school.deleteUser()
            continue
        elif userChoice in 'Qq':
            print('Administrator %s exited!'%user.name)
            break
        else:
            print('No operation math your choice ({}) or operation forbidden(no shcool exists)!'.format(userChoice))
            continue

#老师登录管理函数
def teacherLogin(obj):
    user = userloginCheck('teacher',obj)
    if user == False:
        return
    teacher = user
    teachCourse = teacher.course
    greeting = period()
    print("""
    Good {} teacher [ {} ]

            menu lists

        (G)  : give a lecture
        (VT) : view self information
        (VS) : view students attending class
        (C)  : change password
        (Q)  : quit
            """.format(greeting, user.name))
    while True:
        userChoice = input('Please input your operation: ')
        if userChoice in 'gG':
            teacher.giveLecture()
            continue
        elif userChoice in 'VTvtVtvT':
            courses = obj.getCourses()
            course = courses[teachCourse]
            teacher.showInfo(course)
            continue
        elif userChoice in 'VSvsVsvS':
            studentDict = obj.getUser('student')
            if len(studentDict) > 0:
                try:
                    if len(studentDict[teachCourse]) > 0:
                        print("""
        Students attending {} are as below""".format(teachCourse))
                        print("""
    number   name   age   gender   class""")
                        for student in studentDict[teachCourse]:
                            stu = studentDict[teachCourse][student]
                            print('       {} {}      {}     {}        {}'.format(stu.number,stu.name,stu.age,stu.gender,stu.classof))
                except:
                    print('\nNo students info to show!\n')
            else:
                print('\nNo students info to show!\n')
            continue
        elif userChoice in 'cC':
            teacher.changePassword()
            continue
        elif userChoice in 'qQ':
            print('Teacher %s exited!'%user.name)
            break
        else:
            print('No operation math your choice ({})'.format(userChoice))
#学生登录管理函数
def studentLogin(obj):
    user = userloginCheck('student',obj)
    if user == False:
        return
    student = user
    course = student.classof
    courses = obj.getCourses()
    greeting = period()
    print("""
    Good {}  [ {} ]

            menu lists

        (L) : Learning
        (P) : Pay the fees
        (S) : Self info show
        (C) : change password
        (Q) : quit
            """.format(greeting, user.name))
    while True:
        userChoice = input('Please input your operation: ')
        if userChoice in 'lL':
            student.learning()
            continue
        elif userChoice in 'pP':
            student.payFees()
            continue
        elif userChoice in 'sS':
            course = courses[course]
            student.showInfo(course)
            continue
        elif userChoice in 'cC':
            student.changePassword()
            continue
        elif userChoice in 'qQ':
            print('Student %s exited!'%user.name)
            break
        else:
            print('No operation math your choice ({})'.format(userChoice))

#系统起始运行函数
def systemStart():
    adminFirstLogin = False
    admin = Member('admin','admin','admin','admin')
    school = School()
    school.adminAdd('admin', admin)
    menu = """
    Welcome to education manage system

            menu lists

        (M) : system manage
        (T) : teacher login
        (S) : student login
        (Q) : quit
            """
    print(menu)
    while True:
        userChoice = input('Please input your operation(input "O" for operation menu list) : ')
        if userChoice in 'oO':
            print(menu)
            continue
        if userChoice in 'Mm':
            loginUser = userloginCheck('admin',school)
            if loginUser == False:
                continue
            if adminFirstLogin:
                    systemManage(loginUser,school)
            else:
                print('There is no school exists, please create a school first!\n')
                schoolname = ''; schoollocation = ''; schoolmotto = ''
                while True:
                    if schoolname == '':
                        schoolname = input('Please input your school name : ')
                        if schoolname == '':
                            print('School name can not be blank, please reinput!')
                            continue

                    if schoollocation == '':
                        schoollocation = input('Please input your school location : ')
                        if schoollocation == '':
                            print('School location can not be blank, please reinput!')
                            continue

                    if schoolmotto == '':
                        schoolmotto = input('Please input your school motto : ')
                        if schoolmotto == '':
                            print('School motto can not be blank, please reinput!')
                            continue
                    break
                school.schoolactivate(schoolname, schoollocation, schoolmotto)
                systemManage(loginUser,school)
                adminFirstLogin = True
                continue
        elif userChoice in 'Tt':
            if adminFirstLogin :
                teacherLogin(school)
            else:
                print('There is no school exists, please create a school first(iNput "m|M")!\n')
                continue
        elif userChoice in 'Ss':
            if adminFirstLogin :
                studentLogin(school)
            else:
                print('There is no school exists, please create a school first(iNput "m|M")!\n')
                continue
        elif userChoice in 'Qq':
            break
        else:
            print('No operation math your choice ({})'.format(userChoice))

    print('System exited!')
if __name__ == "__main__":
    systemStart()
