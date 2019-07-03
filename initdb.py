from orm import create_session,SystemPar,SystemCode








def main():
    db_session=create_session()
    _create_db_table()
    db_session.commit()
    SystemPar.delete_all(db_session)
    db_session.commit()
    system_type=''
    if platform.platform().find('Windows')>=0:
        system_type='Windows'
    else:
        system_type='UNIX'
    # 基础数据
    systemPar = SystemPar(par_code='version',
                          par_desc='版本信息', par_value='1.0', par_type=2)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='node_count',
                          par_desc='节点数量', par_value='0', par_type=1)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='edge_count',
                          par_desc='关系数量', par_value='0', par_type=1)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='polling_second',
                          par_desc='Queue轮询间隔秒数', par_value='60', par_type=1)
    db_session.add(systemPar)
    if system_type=='UNIX':
        systemPar = SystemPar(par_code='import_neo4j_install_dir', par_desc='数据导入NEO4J安装目录',
                          par_value='/u01/cqaudit/software/neo4j-enterprise-3.5.6/', par_type=2)
        db_session.add(systemPar)
    else:
        systemPar = SystemPar(par_code='import_neo4j_install_dir', par_desc='数据导入NEO4J安装目录',
                          par_value='D:/software/neo4j-enterprise-3.5.6/', par_type=2)
        db_session.add(systemPar)
    systemPar = SystemPar(par_code='download_batch', par_desc='从远程服务器下载数据的批量',
                          par_value='10000', par_type=1)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='csv_batch', par_desc='读取和写入csv的批量',
                          par_value='10000', par_type=1)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='neo4j_status', par_desc='NEO4J状态',
                          par_value='未知', par_type=2)  # 可以为未知、启动中，运行中、关闭中，已关闭
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='import_status',
                          par_desc='导入状态', par_value='空闲', par_type=2)  # 空闲、导入中
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='neo4j_last_import_datetime',
                          par_desc='NEO4J数据最后更新时间', par_value='2019-06-07 12:44:44.0000', par_type=4)
    db_session.add(systemPar)
    SystemCode.delete_all(db_session)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='CNY', code_value='人民币元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='HKD', code_value='港元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='JPY', code_value='日圆', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='SUR', code_value='卢布', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='CAD', code_value='加元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='USD', code_value='美元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='AUD', code_value='澳大利亚元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='NZD', code_value='新西兰元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='SGD', code_value='新加坡元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='process_type', code_desc='任务类型',
                            code_code='systest', code_value='系统测试', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='process_type', code_desc='任务类型',
                            code_code='basedataimport', code_value='基础数据采集', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='process_type', code_desc='任务类型',
                            code_code='customizedataimport', code_value='自定义数据采集', code_type=2)
    db_session.add(systemCode)
    # 节点色彩
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='FFFFCC', code_value='FFFFCC', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='CCFFFF', code_value='CCFFFF', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='FFCCCC', code_value='FFCCCC', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='CCCCFF', code_value='CCCCFF', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='99CCCC', code_value='99CCCC', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='99CCFF', code_value='99CCFF', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='CCCCCC', code_value='CCCCCC', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='CCCC99', code_value='CCCC99', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='3399CC', code_value='3399CC', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='FFCC99', code_value='FFCC99', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='node_color', code_desc='节点色彩',
                            code_code='99CC33', code_value='99CC33', code_type=2)
    db_session.add(systemCode)
    db_session.commit()

    # 测试数据
    processDetail = ProcessDetail(pd_uuid=str(uuid.uuid1()), pd_start_datetime=datetime.datetime.now(), pd_catalog='systest',
                                  pd_command='SQL1Annotations are a concept used internally by SQLAlchemy in order to store additional information along with ClauseElement objects. A Python dictionary is associated with a copy of the object, which contains key/value pairs significant to various internal systems, mostly within the ORM:')
    db_session.add(processDetail)
    systemData = SystemData(sys_uuid=str(uuid.uuid1(
    )), sys_name='统一社会编码的法人机构', sys_end_date=datetime.datetime.now(), sys_count=10000)
    db_session.add(systemData)
    systemData = SystemData(sys_uuid=str(uuid.uuid1(
    )), sys_name='自然人', sys_end_date=datetime.datetime.now(), sys_count=30000)
    db_session.add(systemData)

    queue = JobQueue(u_uuid=str(uuid.uuid1()), u_declare_key='test', u_body='test body', u_publisher_id='a',
                     u_publish_datetime=datetime.datetime.now(), u_no_ack=False, u_start_datetime=datetime.datetime.now())
    db_session.add(queue)
    db_session.commit()
    print('init db ok')
    db_session.close()



if __name__ == '__main__':
    main()
    # print(__name__)