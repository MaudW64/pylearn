# python不支援函式重載(overload) 之解決方式：設定引數

"""
# def方式一
def account (name,number,balance=0):  # balance=0 為 預設引數
    print(name,number,balance)
"""
# def方式二
def account (**data):  # 參考TestDef4
    print(data.get('name'),data.get('number'),data.get('balance'))

account(name='東東',number='0001-0001',balance=100)
account(name='西西',number='0001-0001')
account(name='南南')
