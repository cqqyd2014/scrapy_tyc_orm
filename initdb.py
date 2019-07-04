from orm import create_session,SystemPar,SystemCode,_create_db_table
import platform







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
    
    if system_type=='UNIX':
        systemPar = SystemPar(par_code='import_neo4j_install_dir', par_desc='数据导入NEO4J安装目录',
                          par_value='/u01/cqaudit/software/neo4j-enterprise-3.5.6/', par_type=2)
        db_session.add(systemPar)
    else:
        systemPar = SystemPar(par_code='import_neo4j_install_dir', par_desc='数据导入NEO4J安装目录',
                          par_value='D:/software/neo4j-enterprise-3.5.6/', par_type=2)
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
    
    db_session.commit()

    # 测试数据
    
    db_session.commit()
    print('init db ok')
    db_session.close()



if __name__ == '__main__':
    main()
    # print(__name__)