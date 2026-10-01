import math
total=0
price_peyk=0
name=''
shomare=''
address=''
total_frosh=0
total_kharid=0
total_hazine=0
total_hqoq=0
while True:
    kababi_mohamd_tala=input(''' ----KABABI MOHAMMAD TALA----
        1. kobide
        2.salad 
        3.noshabe 
        4.pik motori 
        5.call center
        6.factor
        7.hesabdari
        ''')
    if kababi_mohamd_tala in [1,2,3,4,5,6,7]:
         kababi_mohamd_tala=int(kababi_mohamd_tala)
         break
    else:
         print('pls enter number 1 to 7... ')

    #kobide
    if kababi_mohamd_tala==1:
    
            print('---- MENEU----')
            kobide=(
            '1.kobide ngigni chili ',
            '2.kobide ngini espysi' ,
            '3.kobide ngini kham'
            )

            for x in range(len(kobide)):
                 print(x+1,kobide[x])

            price_kobide=[]
            for x in range(len(kobide)):
                 price=int(input(f'price {kobide[x]}: '))
                 price_kobide.append(price)

            mneu=int(input('entekhab konid->'))
            tedad=int(input('chand add?'))


            if mneu==1:
                mablaq=price_kobide[0]*tedad

            elif mneu==2:
                mablaq=price_kobide[1]*tedad

            elif mneu==3:
                mablaq=price_kobide[2]*tedad
            else:
                print('eshtbah entkhab kardid')

            total=total+mablaq
            print(f'''
            mablaq: {mablaq}
            total: {total}''')
    
    #salad
    elif kababi_mohamd_tala==2:
        print('----SALAD----')
        salad=(
        '1.salad shirazi ba abqore sonati',
        '2.salad fasl'
        )
        for x in range(len(salad)):
             print(x+1,salad[x])

        price_salad=[]
        for x in range(len(salad)):
             price=int(input(f'price {salad[x]}: '))
             price_salad.append(price)

        salad=int(input('entkhab konid->'))
        tedad=int(input('chand add?'))

        if salad==1:
            mablaq=price_salad[0]*tedad

        elif salad==2:
            mablaq=price_salad[1]*tedad
        else:
            print('eshtbah entkhab kardid')

        total=total+mablaq

        print(f'''
        mablaq: {mablaq}
        total: {total}''')
        
    

    #noshabe
    elif kababi_mohamd_tala==3:
            print=('----NOSHABE----')
            noshabe=(
            '1.fanta'
            '2.kola'
            '3.miranda'
            )

            for x in range(len(noshabe)):
                 print(x+1,noshabe[x])

            price_noshabe=[]
            for x in range(len(noshabe)):
                 price=int(input(f'price{noshabe[x]}: '))
                 price_noshabe.append(price)
            mneu_noshabe=int(input('entekhab konid-> '))
            tedad=int(input('chand add? '))

            if mneu_noshabe==1:
                mablaq=price_noshabe[0]*tedad

            elif mneu_noshabe==2:
                mablaq=price_noshabe[1]*tedad

            elif mneu_noshabe==3:
                mablaq=price_noshabe[2]*tedad

            else:
                 print('eshtbah entkhab kardid')

            total=total+mablaq

            print(f'''
            mablaq: {mablaq}
            total: {total}''')


    #pyk motori
    elif kababi_mohamd_tala==4:
            print('----PyK MOTORI----')
            name=input('enter your name and family->')
            shomare=int(input('enter mobile number->'))
            address=input('address ?')
            masafat=float(input('masafat be Km? '))
            if masafat<=5:
                price_peyk=0
                print('price pyk: free (up to 5Km)')
            else:
                 price_peyk=math.round((masafat-5)*10000)
                 print(f'price pyk:{price_peyk} ')

            total=total+price_peyk
    
            print(f'''  ***FACTOR PyK***
            name : {name}
            phone: {shomare}
            address: {address}
            masafat: {masafat}km
            mablq peyk: {price_peyk}''')

    #call center
    elif kababi_mohamd_tala==5:
            name=input('enter your nam and family? ')
            address=input('enter your address?  ')
            shomare=input('enter mobile number? ')
            sefaresh=input('enter sefaresh-----')
            print(f'''----call center----
            name: {name}
            phone: {shomare}
            address: {address}
            sefaresh: {sefaresh}
            sefsresh sabt shodヾ(⌐■_■)ノ♪''')

    #factor
    elif kababi_mohamd_tala==6:
            maliat=math.round(total*0.1)
            mablaq_kol=total+maliat
            
            print(f'''
            ---factor---
            name moshtari: {name}
            call number: {shomare}
            address: {address}
            -----------------------------
            mablaq qaza: {total}
            mablaq pik motori: {price_peyk}
            maliat 10%: {maliat}
            -----------------------------
            mablaq kol: {mablaq_kol}''')
    #hesabdari
    elif kababi_mohamd_tala==7:
        while True:
            hesabdari=input('''
            -----HESABDARI-----
            1.frosh
            2.kharid
            3.hazine
            4.hqoq
            5.sod
            6.gozarersh
            7.back
            entekhab konid-> ''')
            if hesabdari in ['1', '2', '3', '4', '5', '6', '7']:
                hesabdari=int(hesabdari)
                break
            else:
                print("pls enter number 1 to 7...")
            # frosh hesabdari
            if hesabdari==1:
                print(F'''
                ----FROSH---
                TOTAL FROSH: {total_frosh}''')
            #kharid hesabdari
            elif hesabdari==2:
                kharid=int(input('''
                    ----KHARID----
                    1.gosht
                    2.brenj
                    3.nan
                    4.noshabe
                    entekhab konid-> '''))
                
                if kharid==1:
                    kala='gosht'
                elif kharid==2:
                    kala='brenj'
                elif kharid==3:
                    kala='nan'
                elif kharid==4:
                    kala='noshabe'
                else:
                    print('entekhab eshtbah ast')
                
                price_kharid=float(input('mablaq kharid? '))
                tedad_kharid=int(input('chand add? '))
                mablaq_kharid=price_kharid*tedad_kharid
                total_kharid=total_kharid+mablaq_kharid

                print(f'''
                    kala: {kala}
                    tedad: {tedad_kharid}
                    mablaq kharid: {mablaq_kharid}
                    jam kharid: {total_kharid}''')
            #hazine hesabdari
            elif hesabdari==3:
                hazine=int(input('''
                    ----HAZINE----
                    1.ejare
                    2.barq
                    3.ab
                    4.gaz
                    5.tamirat
                    entekhab konid->'''))
                if hazine==1:
                    noe_hazine='ejare'
                elif hazine==2:
                    noe_hazine='barnq'
                elif hazine==3:
                    noe_hazine='ab'
                elif hazine==4:
                    noe_hazine='gaz'
                elif hazine==5:
                    noe_hazine='tamirat'
                else:
                    print('entekhab eshtebsh ast')

                mablaq_hazine=float(input('mablaq hazine? '))
                total_hazine=total_hazine+mablaq_hazine

                print(f'''
                    noe hazine: {noe_hazine}
                    mablaq: {mablaq_hazine}
                    majmo hazine ha: {total_hazine}''')
            #hqoq hesabdari
            elif hesabdari==4:
                karmand=int(input('''
                    ----HOQOQ----
                    1.ashpaz
                    2.garson
                    3.pyk
                    4.sandogh dar'''))
                if karmand==1:
                    shoql='ashpaz'
                elif karmand==2:
                    shoql='garson'
                elif karmand==3:
                    shoql='pyk'
                elif karmand==4:
                    shoql='sandogh dar'
                else:
                    print('entekhab eshtebah ast')

                hqoq=float(input('hqoq karmand?? '))
                ezafe_kari=float(input('teddad saat ezafe kari?? '))
                price_saat_ezafe=100000

                mablaq_ezafe=ezafe_kari*price_saat_ezafe
                mblaq_kol_hqoq=hqoq+mablaq_ezafe
                total_hqoq=total_hqoq+mblaq_kol_hqoq

                print(f'''
                    karman: {shoql}
                    hqoq: {hqoq}
                    saat ezafe kari: {ezafe_kari}
                    mablaq ezafe kari: {mablaq_ezafe}
                    mablaq kol hqoq: {mblaq_kol_hqoq}''')

            # sod o zian hesabdari     
            elif hesabdari==5:
                sod=total_frosh-total_kharid-total_hazine-total_hqoq
                print(f'''
                    =================
                        SOD & ZIAN 
                        ''')

                if sod>0:
                    print(f'sod shoma: {sod}')
                elif sod<0:
                    print(f'zarar shoma: {abs(sod)}')
                else:
                    print('sod o zarar ndarid')
            # gozaresh hesabdari
            elif hesabdari==6:
                sod=total_frosh-total_kharid-total_hazine-total_hqoq
                print(f'''
                        **GOZARESH MALI**
                    **KABABI MOHAMAD TALA**
                    
                    total frosh: {total_frosh}
                    total kharid: {total_kharid}
                    total hazine: {total_hazine}
                    total hqoq: {total_hqoq}

                    sod o zian: {sod}''')
            #khroj az hesabdari
            elif hesabdari==7:
                break

            else:
                print('entkhab eshtbah ast')

    x=input('ensert exit for end->')
    if x.lower()=='exit':
            break
    else:
         print('pls enter exit')

