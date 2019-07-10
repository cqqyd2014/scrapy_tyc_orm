
# 公共模块

import platform
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, Float, Text, Date, Boolean
import datetime
import uuid
import json
from python_common.common import DateTimeEncoder


postgresql_conn_str = "postgresql+psycopg2://postgres:Wang1980@localhost:33133/tyc"
engine = create_engine(postgresql_conn_str, isolation_level = 'READ COMMITTED')

# mysql_conn_str='mysql+mysqldb://root:Wang1980@localhost:3306/mosr?charset=utf8mb4'
# engine=create_engine(mysql_conn_str)
Base = declarative_base()


def _create_db_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_session():

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


class SystemPar(Base):
    __tablename__ = "system_par"
    par_code = Column(String(64), primary_key=True)
    par_desc = Column(String(128))
    par_value = Column(String(1024))
    par_type = Column(Integer)  # 1为数字2为文本3为日期4为日期时间（含毫秒）

    @staticmethod
    def delete_all(db_session):
        db_session.query(SystemPar).delete()

    def __repr__(self):
        return self.par_code+"_"+self.par_value

    def to_json(self):
        json_string = {
            'par_code': self.par_code,
            'par_desc': self.par_desc,
            'par_value': self.par_value,
            'par_type': self.par_type

        }
        return json_string

    @staticmethod
    def from_json(json_string):
        return SystemPar(par_code=json_string.get('par_code'), par_desc=json_string.get('par_desc'), par_value=json_string.get('par_value'), par_type=json_string.get('par_type'))

class SystemCode(Base):
    __tablename__ = "system_code"
    code_main = Column(String(64), primary_key=True)
    code_desc = Column(String(256))
    code_code = Column(String(128), primary_key=True, unique=True)
    code_value = Column(String(1024))
    code_type = Column(Integer)  # 1为数字2为文本3为日期4为日期时间（含毫秒）

    def to_json(self):
        json_string = {
            'code_main': self.code_main,
            'code_desc': self.code_desc,
            'code_code': self.code_code,
            'code_value': self.code_value,
            'code_type': self.code_type,

        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(SystemCode).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(SystemCode).filter(
            SystemCode.code_main == self.code_main, SystemCode.code_code == self.code_code).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.code_desc = self.code_desc
            db_data.code_value = self.code_value
            db_data.f_trade = self.f_trade
            db_data.code_type = self.code_type

class CompanyChangeLog(Base):
    __tablename__ = "compnay_change_log"
    c_change_order=Column(Integer, primary_key=True)
    c_change_date=Column(Date)
    c_change_item=Column(String(512))

    c_change_before=Column(Text)
    c_change_after=Column(Text)

    c_company_id=Column(String(64), primary_key=True)

    
    def saveOfUpdate(self, session):
        db_data = session.query(CompanyChangeLog).filter(
            CompanyChangeLog.c_company_id == self.c_company_id,CompanyChangeLog.c_change_order==self.c_change_order).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.c_change_date=self.c_change_date
            db_data.c_change_item=self.c_change_item
            db_data.c_change_before=self.c_change_before
            db_data.c_change_after=self.c_change_after
            



    @staticmethod
    def delete_all(db_session):
        db_session.query(CompanyChangeLog).all().delete()
        #print("删除成功")


    def __repr__(self):
        return self.c_company_id+self.c_change_order

    def to_json(self):
        json_string = {
            'c_company_id': self.c_company_id,
            'c_change_order': self.c_change_order,
            'c_change_date':json.dumps(self.c_change_date, cls=DateTimeEncoder),
            'c_change_item':self.c_change_item,
            'c_change_before':self.c_change_before,
            'c_change_after': self.c_change_after,
            

        }
        return json_string

class CompanyMainMember(Base):
    __tablename__ = "compnay_main_meber"
    c_member_order=Column(Integer, primary_key=True)
    c_member_id=Column(String(512))
    c_member_href=Column(String(1024))
    c_member_type=Column(String(512))
    c_member_job=Column(String(512))
    c_member_name=Column(String(512))

    c_company_id=Column(String(64), primary_key=True)

    
    def saveOfUpdate(self, session):
        db_data = session.query(CompanyMainMember).filter(
            CompanyMainMember.c_company_id == self.c_company_id,CompanyMainMember.c_member_order==self.c_member_order).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.c_member_id=self.c_member_id
            db_data.c_member_href=self.c_member_href
            db_data.c_member_type=self.c_member_type
            db_data.c_member_job=self.c_member_job
            db_data.c_member_name=self.c_member_name
            
            



    @staticmethod
    def delete_all(db_session):
        db_session.query(CompanyMainMember).all().delete()
        #print("删除成功")


    def __repr__(self):
        return self.c_company_id+self.c_member_order

    def to_json(self):
        json_string = {
            'c_company_id': self.c_company_id,
            'c_member_order': self.c_member_order,
            'c_member_name':self.c_member_name,
            'c_member_id':self.c_member_id,
            'c_member_href':self.c_member_href,
            'c_member_type': self.c_member_type,
            'c_member_job': self.c_member_job,
            

        }
        return json_string


class CompanyShareholderInfo(Base):
    __tablename__ = "company_shareholder_info"
    c_shareholder_order=Column(Integer, primary_key=True)
    c_shareholder_name=Column(String(512))
    c_company_id=Column(String(512))
    c_shareholder_id=Column(String(512))
    c_shareholder_href=Column(String(1024))
    c_shareholder_percent=Column(Numeric)
    c_shareholder_amount=Column(Numeric)
    c_shareholder_type=Column(String(64))#company#human
    
    
    c_company_id=Column(String(64), primary_key=True)

    
    def saveOfUpdate(self, session):
        db_data = session.query(CompanyShareholderInfo).filter(
            CompanyShareholderInfo.c_company_id == self.c_company_id,CompanyShareholderInfo.c_shareholder_order==self.c_shareholder_order).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.c_shareholder_order=self.c_shareholder_order
            db_data.c_shareholder_name=self.c_shareholder_name
            db_data.c_shareholder_href=self.c_shareholder_href
            db_data.c_shareholder_percent=self.c_shareholder_percent
            db_data.c_shareholder_amount=self.c_shareholder_amount
            db_data.c_company_id=self.c_company_id
            db_data.c_shareholder_type=self.c_shareholder_type
            db_data.c_tianyancha_id=self.c_tianyancha_id
            db_data.c_shareholder_id=self.c_shareholder_id



    @staticmethod
    def delete_all(db_session):
        db_session.query(CurrentShareholderInfo).all().delete()
        #print("删除成功")


    def __repr__(self):
        return self.c_company_id+self.c_shareholder_order+'/'+self.c_shareholder_name

    def to_json(self):
        json_string = {
            'c_company_id': self.c_company_id,
            'c_shareholder_order': self.c_shareholder_order,
            'c_shareholder_name':self.c_shareholder_name,
            'c_shareholder_href':self.c_shareholder_href,
            'c_shareholder_amount':self.c_shareholder_amount,
            'c_shareholder_percent': self.c_shareholder_percent,
            'c_shareholder_type':self.c_shareholder_type,
            'c_tianyancha_id':self.c_tianyancha_id

        }
        return json_string


class CompanyBaseInfo(Base):
    __tablename__ = "company_base_info"
    c_lawman_id=Column(String(64))
    c_lawman_name=Column(String(128))
    c_lawman_href=Column(String(1024))
    c_name=Column(String(1024), unique=True)
    c_uscc=Column(String(64), unique=True)#统一社会信用代码
    c_reg_capital=Column(Numeric)
    c_real_capital=Column(Numeric)
    c_start_date=Column(Date)
    c_status=Column(String(64))
    c_tax_code=Column(String(64))
    c_org_code=Column(String(64))
    c_reg_code=Column(String(64))#工商注册号
    c_type=Column(String(64))
    c_industry=Column(String(64))
    c_permit_date=Column(Date)
    c_permit_gov=Column(String(512))
    c_business_period=Column(String(512))
    c_tax_level=Column(String(512))
    c_staff=Column(String(512))
    c_old_name=Column(String(512))
    c_english_name=Column(String(1024))#英文名称
    c_social_security_staff=Column(Integer)#参保人数
    c_addr=Column(String(1024))
    c_business=Column(Text)
    c_company_id=Column(String(64), primary_key=True)
    c_tianyancha_link=Column(String(1024))

    
    def saveOfUpdate(self, session):
        db_data = session.query(CompanyBaseInfo).filter(
            CompanyBaseInfo.c_company_id == self.c_company_id).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.c_name=self.c_name
            db_data.c_uscc=self.c_uscc
            db_data.c_reg_capital=self.c_reg_capital
            db_data.c_real_capital=self.c_real_capital
            db_data.c_start_date=self.c_start_date
            db_data.c_status=self.c_status
            db_data.c_tax_code=self.c_tax_code
            db_data.c_org_code=self.c_org_code
            db_data.c_reg_code=self.c_reg_code
            db_data.c_type=self.c_type
            db_data.c_industry=self.c_industry
            db_data.c_permit_date=self.c_permit_date
            db_data.c_permit_gov=self.c_permit_gov
            db_data.c_business_period=self.c_business_period
            db_data.c_tax_level=self.c_tax_level
            db_data.c_staff=self.c_staff
            db_data.c_old_name=self.c_old_name
            db_data.c_english_name=self.c_english_name
            db_data.c_social_security_staff=self.c_social_security_staff
            db_data.c_addr=self.c_addr
            db_data.c_business=self.c_business
            db_data.c_company_id=self.c_company_id
            db_data.c_tianyancha_link=self.c_tianyancha_link
            db_data.c_lawman_id=self.c_lawman_id
            db_data.c_lawman_name=self.c_lawman_name
            db_data.c_lawman_href=self.c_lawman_href



    @staticmethod
    def delete_all(db_session):
        db_session.query(CompanyBaseInfo).all().delete()
        #print("删除成功")


    def __repr__(self):
        return self.c_name+self.c_uscc+'/'+self.c_tianyancha_company_id

    def to_json(self):
        json_string = {
            'c_company_id': self.c_company_id,
            'c_name': self.c_name,
            'c_reg_capital':self.c_reg_capital,
            'c_real_capital':self.c_real_capital,
            'c_tianyancha_link':self.c_tianyancha_link,
            'c_start_date': json.dumps(self.c_start_date, cls=DateTimeEncoder),
            'c_lawman_id': self.c_lawman_id,
            'c_lawman_name': self.c_lawman_name,
            'c_lawman_href': self.c_lawman_href,
            'c_uscc': self.c_uscc,
            'c_status': self.c_status,
            'c_tax_code': self.c_tax_code,
            'c_org_code': self.c_org_code,
            'c_reg_code': self.c_reg_code,
            'c_type': self.c_type,

            

        }
        return json_string



'''
#当前系统中的节点标签
class CurrentNodeLabels(Base):
    __tablename__ = "current_node_labels"
    labels = Column(String(1024), primary_key=True)
    label = Column(String(1024), primary_key=True)
    create_datetime=Column(DateTime)
    

    @staticmethod
    def saveOfUpdate(self, session):
        db_data = session.query(CurrentNodeLabels).filter(
            CurrentNodeLabels.labels == self.labels, CurrentNodeLabels.label == self.label).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            pass

    @staticmethod
    def delete_all(db_session):
        db_session.query(CurrentNodeLabels).delete()
        #print("删除成功")


    def __repr__(self):
        return self.labels+self.label

    def to_json(self):
        json_string = {
            'labels': self.labels,
            'label': self.label,
            'create_datetime': json.dumps(self.create_datetime, cls=DateTimeEncoder),
            

        }
        return json_string


#当前系统中的关系类型
class CurrentEdgeTyps(Base):
    __tablename__ = "current_edge_types"
    edge_type = Column(String(1024), primary_key=True)
    create_datetime=Column(DateTime)


    
    

    @staticmethod
    def saveOfUpdate(self, session):
        db_data = session.query(CurrentEdgeTyps).filter(
            CurrentEdgeTyps.edge_type == self.edge_type).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            pass

    @staticmethod
    def delete_all(db_session):
        db_session.query(CurrentEdgeTyps).delete()

        


    def __repr__(self):
        return self.edge_type

    def to_json(self):
        json_string = {
            'edge_type': self.edge_type,
            'create_datetime': json.dumps(self.create_datetime, cls=DateTimeEncoder),
            

        }
        return json_string

#当前系统中的属性
class CurrentProperties(Base):
    __tablename__ = "current_properties"
    u_uuid=Column(String(37), primary_key=True)
    u_type = Column(String(32))
    u_label_type=Column(String(512))
    u_column_name=Column(String(512))
    u_column_type=Column(String(512))
    create_datetime=Column(DateTime)
    
    

    @staticmethod
    def saveOfUpdate(self, session):
        db_data = session.query(CurrentProperties).filter(
            CurrentProperties.u_uuid == self.u_uuid).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            pass

    @staticmethod
    def delete_all(db_session):
        db_session.query(CurrentProperties).delete()


    def __repr__(self):
        return self.u_uuid
    
    def to_json(self):
        json_string = {
            'u_uuid': self.u_uuid,
            'u_type': self.u_type,
            'u_label_type': self.u_label_type,
            'u_column_name': self.u_column_name,
            'u_column_type': self.u_column_type,
            'create_datetime': json.dumps(self.create_datetime, cls=DateTimeEncoder),
            

        }
        return json_string



# 当前等待导入的数据
class ImportData(Base):
    __tablename__ = "import_data"
    u_uuid = Column(String(37), primary_key=True)
    u_create_datetime = Column(DateTime)
    u_queue_uuid = Column(String(37))
    u_start_download_datetime = Column(DateTime)
    u_end_download_datetime = Column(DateTime)
    u_start_import_datetime = Column(DateTime)
    u_end_import_datetime = Column(DateTime)
    u_node_edge = Column(String(64))
    u_label_items = Column(Text)
    u_edge_type = Column(Text)
    u_column_items = Column(Text)
    u_status = Column(String(64))  # 创建任务，开始下载，下载完成，开始导入，导入完成，已删除
    u_rowcount=Column(Integer)

    @staticmethod
    def saveOfUpdate(self, session):
        db_data = session.query(SystemCode).filter(
            SystemCode.code_main == self.code_main, SystemCode.code_code == self.code_code).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.code_desc = self.code_desc
            db_data.code_value = self.code_value
            db_data.f_trade = self.f_trade
            db_data.code_type = self.code_type

    @staticmethod
    def delete_all(db_session):
        db_session.query(ImportData).delete()

    def __repr__(self):
        return self.u_uuid+self.u_declare_key+self.u_body

    def to_json(self):
        json_string = {
            'u_uuid': self.u_uuid,
            'u_create_datetime': json.dumps(self.u_create_datetime, cls=DateTimeEncoder),
            'u_queue_uuid': self.u_queue_uuid,
            'u_start_download_datetime': json.dumps(self.u_start_download_datetime, cls=DateTimeEncoder),
            'u_end_download_datetime': json.dumps(self.u_end_download_datetime, cls=DateTimeEncoder),
            'u_start_import_datetime': json.dumps(self.u_start_import_datetime, cls=DateTimeEncoder),
            'u_end_import_datetime': json.dumps(self.u_end_import_datetime, cls=DateTimeEncoder),
            'u_node_edge': self.u_node_edge,
            'u_label_items': self.u_label_items,
            'u_edge_type': self.u_edge_type,
            'u_column_items': self.u_column_items,
            'u_status': self.u_status,
            'u_rowcount':self.u_rowcount,




        }
        return json_string


# 任务列表
class JobQueue(Base):
    __tablename__ = "job_queue"
    u_uuid = Column(String(37), primary_key=True)
    u_declare_key = Column(String(256))  # download_data从远程数据库下载数据
    u_body = Column(Text)
    u_publisher_id = Column(String(256))
    u_publish_datetime = Column(DateTime)
    u_no_ack = Column(Boolean)  # 为True的情况，消息一旦接受就认为结束，为False的情况消息需要客户端确认处理完成才结束。
    u_start_datetime = Column(DateTime)  # 开始处理时间
    u_complete_datetime = Column(DateTime)  # 结束处理时间
    u_status = Column(String(16))  # 发布，处理中，处理完成
    u_back_message=Column(Text)

    @staticmethod
    def delete_all(db_session):
        db_session.query(JobQueue).delete()

    def __repr__(self):
        return self.u_uuid+self.u_declare_key+self.u_body

    def to_json(self):
        json_string = {
            'u_uuid': self.u_uuid,
            'u_declare_key': self.u_declare_key,
            'u_body': self.u_body,
            'u_publish_datetime': json.dumps(self.u_publish_datetime, cls=DateTimeEncoder),
            'u_no_ack': self.u_no_ack,
            'u_publisher_id': self.u_publisher_id,
            'u_complete_date': json.dumps(self.u_complete_datetime, cls=DateTimeEncoder),
            'u_status': self.u_status,
            'u_start_datetime': json.dumps(self.u_start_datetime, cls=DateTimeEncoder),
            'u_back_message':self.u_back_message




        }
        return json_string


class SystemDataCorp(Base):
    __tablename__ = "system_data_corp"
    corp_uscc = Column(String(18), primary_key=True)
    corp_name = Column(String(128), unique=True)

    @staticmethod
    def delete_all(db_session):
        db_session.query(SystemDataCorp).delete()

    def __repr__(self):
        return self.corp_name

    def to_json(self):
        json_string = {
            'corp_uscc': self.corp_uscc,
            'corp_name': self.corp_name,


        }
        return json_string

    @staticmethod
    def from_json(json_string):
        return SystemPar(corp_uscc=json_string.get('corp_uscc'), corp_name=json_string.get('corp_name'))


class SystemData(Base):
    __tablename__ = "system_data"
    sys_uuid = Column(String(37), primary_key=True)
    sys_name = Column(String(128), unique=True)
    sys_end_date = Column(Date)
    sys_count = Column(Integer)  # 1为数字2为文本3为日期4为日期时间（含毫秒）

    @staticmethod
    def delete_all(db_session):
        db_session.query(SystemData).delete()

    def __repr__(self):
        return self.sys_name

    def to_json(self):
        json_string = {
            'sys_uuid': self.sys_uuid,
            'sys_name': self.sys_name,
            'sys_end_date': json.dumps(self.sys_end_date, cls=DateTimeEncoder),
            'sys_count': self.sys_count

        }
        return json_string

    @staticmethod
    def from_json(json_string):
        return SystemPar(par_code=json_string.get('sys_uuid'), par_desc=json_string.get('sys_name'), par_value=json_string.get('sys_end_date'), par_type=json_string.get('sys_count'))




class NodeLabelColor(Base):
    __tablename__ = "node_label_color"
    n_lable_classs = Column(String(256), primary_key=True)
    n_color = Column(String(6))
    n_lable_display = Column(String(256), unique=True)

    def to_json(self):
        json_string = {
            'n_lable_classs': self.n_lable_classs,
            'n_color': self.n_color,
            'n_display': self.n_display,


        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(NodeLabelColor).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(NodeLabelColor).filter(
            NodeLabelColor.n_lable_classs == self.n_lable_classs).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.n_color = self.n_color
            db_data.n_display = self.n_display



class Neno4jCatalog(Base):
    __tablename__ = "neo4j_catlog"
    nc_uuid = Column(String(37), primary_key=True)
    nc_update_datetime = Column(DateTime)
    nc_type = Column(String(64))
    nc_value = Column(String(512))

    def to_json(self):

        json_string = {
            'nc_uuid': self.nc_uuid,
            'nc_update_datetime': json.dumps(self.nc_update_datetime, cls=DateTimeEncoder),
            'nc_type': self.nc_type,
            'nc_value': self.nc_value,


        }

        return json_string


class QueryTemplate(Base):
    __tablename__ = "query_template"
    qt_uuid = Column(String(37), primary_key=True)
    qt_datetime = Column(DateTime)
    qt_object = Column(Text)
    qt_cypher = Column(Text)
    qt_title = Column(String(1024))
    qt_desc = Column(Text)
    qt_type = Column(String(64))

    def to_json(self):

        json_string = {
            'qt_uuid': self.qt_uuid,
            'qt_datetime': json.dumps(self.qt_datetime, cls=DateTimeEncoder),
            'qt_object': self.qt_object,
            'qt_cypher': self.qt_cypher,
            'qt_title': self.qt_title,
            'qt_desc': self.qt_desc,
            'qt_type': self.qt_type

        }

        return json_string


class ProcessDetail(Base):
    __tablename__ = "process_detail"
    pd_uuid = Column(String(37), primary_key=True)
    pd_start_datetime = Column(DateTime)
    pd_catalog = Column(String(32), ForeignKey('system_code.code_code'))
    pd_command = Column(Text)

    def to_json(self):

        json_string = {
            'pd_uuid': self.pd_uuid,
            'pd_start_datetime': json.dumps(self.pd_start_datetime, cls=DateTimeEncoder),
            'pd_catalog': self.pd_catalog,
            'pd_command': self.pd_command,

        }

        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(ProcessDetail).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(ProcessDetail).filter(
            ProcessDetail.pd_uuid == self.pd_uuid).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.pd_start_datetime = self.pd_start_datetime
            db_data.pd_catalog = self.pd_catalog
            db_data.pd_command = self.pd_command



'''

