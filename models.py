# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class ChatRoutine(db.Model):
    __tablename__ = 'chat_routine'

    crid = db.Column(db.Integer, primary_key=True, info='채팅 루틴 고유 인덱스')
    ugid = db.Column(db.ForeignKey('user_group.ugid'), nullable=False, index=True, info='사용자 그룹 고유 인덱스')
    name = db.Column(db.String(50), nullable=False, info='해당 루틴 이름')
    descript = db.Column(db.String(500), info='설명')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')
    updateDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='업데이트 날짜')

    user_group = db.relationship('UserGroup', primaryjoin='ChatRoutine.ugid == UserGroup.ugid', backref='chat_routines')



class ChatRoutineAnalytic(db.Model):
    __tablename__ = 'chat_routine_analytics'

    craid = db.Column(db.Integer, primary_key=True, info='채팅 과정 분석 고유 인덱스')
    crid = db.Column(db.ForeignKey('chat_routine.crid'), nullable=False, index=True, info='채팅 루틴 고유 인덱스')
    analytics = db.Column(db.String(collation='utf8mb4_bin'), nullable=False, info='분석 결과')
    version = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='분석 버전')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')

    chat_routine = db.relationship('ChatRoutine', primaryjoin='ChatRoutineAnalytic.crid == ChatRoutine.crid', backref='chat_routine_analytics')



class ChatRoutineItem(db.Model):
    __tablename__ = 'chat_routine_item'

    criid = db.Column(db.Integer, primary_key=True, info='대화 과정 개별 아이템 고유 인덱스')
    crid = db.Column(db.ForeignKey('chat_routine.crid'), nullable=False, index=True, info='채팅 루틴 고유 인덱스')
    pid = db.Column(db.ForeignKey('plugin.pid'), nullable=False, index=True, info='플러그인 고유 인덱스')
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='대화 과정 처리 순서')

    chat_routine = db.relationship('ChatRoutine', primaryjoin='ChatRoutineItem.crid == ChatRoutine.crid', backref='chat_routine_items')
    plugin = db.relationship('Plugin', primaryjoin='ChatRoutineItem.pid == Plugin.pid', backref='chat_routine_items')



class ChatRoutineLog(db.Model):
    __tablename__ = 'chat_routine_log'

    crlid = db.Column(db.Integer, primary_key=True, info='대화 과정 분석 고유 인덱스')
    crid = db.Column(db.ForeignKey('chat_routine.crid'), db.ForeignKey('chat_routine.crid'), db.ForeignKey('chat_routine.crid'), nullable=False, index=True, info='채팅 루틴 고유 인덱스')
    user_key = db.Column(db.String(50), nullable=False, info='카카오톡 유저 코드')
    triggered_by = db.Column(db.String(1000), nullable=False, info='사용자 입력 내용')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')

    chat_routine = db.relationship('ChatRoutine', primaryjoin='ChatRoutineLog.crid == ChatRoutine.crid', backref='chatroutine_chatroutine_chat_routine_logs')
    chat_routine1 = db.relationship('ChatRoutine', primaryjoin='ChatRoutineLog.crid == ChatRoutine.crid', backref='chatroutine_chatroutine_chat_routine_logs_0')
    chat_routine2 = db.relationship('ChatRoutine', primaryjoin='ChatRoutineLog.crid == ChatRoutine.crid', backref='chatroutine_chatroutine_chat_routine_logs')



class ChatTrigger(db.Model):
    __tablename__ = 'chat_trigger'

    ctid = db.Column(db.Integer, primary_key=True, info='대화 트리거 고유 인덱스')
    crid = db.Column(db.ForeignKey('chat_routine.crid'), nullable=False, index=True, info='채팅 루틴 고유 인덱스')
    input = db.Column(db.String(1000), nullable=False, info='사용자 입력 내용')

    chat_routine = db.relationship('ChatRoutine', primaryjoin='ChatTrigger.crid == ChatRoutine.crid', backref='chat_triggers')



class Plugin(db.Model):
    __tablename__ = 'plugin'

    pid = db.Column(db.Integer, primary_key=True, info='플러그인 고유 인덱스')
    ugid = db.Column(db.ForeignKey('user_group.ugid'), nullable=False, index=True, info='사용자 그룹 고유 인덱스')
    srid = db.Column(db.ForeignKey('system_resource.srid'), nullable=False, index=True, info='시스템 자원 프리셋 고유 인덱스')
    descript = db.Column(db.String(100), nullable=False, info='설명')
    name = db.Column(db.String(100), nullable=False, info='플러그인 이름')
    port = db.Column(db.Integer, nullable=False, info='해당 플러그인이 사용될 내부포트 번호')
    url = db.Column(db.String(500), nullable=False, info='해당 플러그인 clone 할 repo 주소')
    env = db.Column(db.Text, info='해당 플러그인에 사용될 env내용')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')
    updateDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='업데이트 날짜')

    system_resource = db.relationship('SystemResource', primaryjoin='Plugin.srid == SystemResource.srid', backref='plugins')
    user_group = db.relationship('UserGroup', primaryjoin='Plugin.ugid == UserGroup.ugid', backref='plugins')



class Role(db.Model):
    __tablename__ = 'role'

    rid = db.Column(db.Integer, primary_key=True, info='권한 고유 인덱스')
    name = db.Column(db.String(50), nullable=False, info='권한 이름')
    level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='권한 레벨, 0: 슈퍼유저')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')
    updateDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='업데이트 날짜')



class Schedule(db.Model):
    __tablename__ = 'schedule'

    sid = db.Column(db.Integer, primary_key=True, info='스케쥴 고유 인덱스')
    ugid = db.Column(db.ForeignKey('user_group.ugid'), nullable=False, index=True, info='사용자 그룹 고유 인덱스')
    name = db.Column(db.String(50), nullable=False, info='스케쥴 이름')
    days_of_the_week = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='활성 요일')
    start_time = db.Column(db.Time, info='시작 시간')
    end_time = db.Column(db.Time, info='마감 시간')
    start_date = db.Column(db.Date, info='시작 날짜')
    end_date = db.Column(db.Date, info='마감 날짜')
    descript = db.Column(db.Text, info='내용')

    user_group = db.relationship('UserGroup', primaryjoin='Schedule.ugid == UserGroup.ugid', backref='schedules')



class SysLog(db.Model):
    __tablename__ = 'sys_log'

    slid = db.Column(db.Integer, primary_key=True, info='로그 고유 인덱스')
    level = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='로그 레벨')
    _from = db.Column('from', db.String(10), nullable=False, server_default=db.FetchedValue(), info='로그 주체자')
    category = db.Column(db.String(10), nullable=False, info='로그 필터링 옵션')
    feature = db.Column(db.String(10), nullable=False, info='로그 발생 기능')
    descript = db.Column(db.Text, nullable=False, info='내용')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')



class SystemEnv(db.Model):
    __tablename__ = 'system_env'

    seid = db.Column(db.Integer, primary_key=True, info='시스템 변수 고유 인덱스')
    key = db.Column(db.String(50), nullable=False, info='시스템 변수 키')
    val = db.Column(db.String(1000), nullable=False, info='시스템 변수 값')



class SystemResource(db.Model):
    __tablename__ = 'system_resource'

    srid = db.Column(db.Integer, primary_key=True, info='시스템 자원 프리셋 고유 인덱스')
    name = db.Column(db.String(50), nullable=False, info='해당 자원 이름')
    cpu = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='cpu 점유량')
    ram = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue(), info='ram 점유량')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')



class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True, info='사용자 고유 인덱스')
    ugid = db.Column(db.ForeignKey('user_group.ugid'), nullable=False, index=True, info='사용자 그룹 고유 인덱스')
    isVerified = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='인증된 사용자 여부')
    name = db.Column(db.String(50), nullable=False, info='사용자 이름')
    id = db.Column(db.String(50), nullable=False, info='사용자 ID')
    pw = db.Column(db.String(600), nullable=False, info='sha512 일방향 암호화 비밀번호')
    phone = db.Column(db.String(50), info='연락처')
    email = db.Column(db.String(50), info='이메일 주소')
    profileImg = db.Column(db.String(1000), info='사용자 프로필 이미지')
    isDeleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='사용자 삭제됨 여부 (논리적)')
    immortality = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='삭제 불가 여부')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록 날짜')
    updateDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='업데이트 날짜')

    user_group = db.relationship('UserGroup', primaryjoin='User.ugid == UserGroup.ugid', backref='users')



class UserGroup(db.Model):
    __tablename__ = 'user_group'

    ugid = db.Column(db.Integer, primary_key=True, info='사용자 그룹 고유 인덱스')
    rid = db.Column(db.ForeignKey('role.rid'), nullable=False, index=True, info='권한 고유 인덱스')
    name = db.Column(db.String(50), nullable=False, info='그룹 이름')
    immortality = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='삭제 가능 여부')
    registerDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='등록날짜')
    updateDatetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='업데이트 날짜')

    role = db.relationship('Role', primaryjoin='UserGroup.rid == Role.rid', backref='user_groups')
