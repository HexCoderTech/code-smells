def process_data(data):
    result = []
    for item in data:
        if item['status'] == 'active':
            if item['type'] == 'email':
                email = item['email']
                if email.endswith('@gmail.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@hotmail.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@aol.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@outlook.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@icloud.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@protonmail.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@tutanota.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@mail.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yandex.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@zoho.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@gmx.com'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@web.de'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.co.uk'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.ca'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.de'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.fr'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.it'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.es'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif email.endswith('@yahoo.in'):
                    name, domain = email.split('@')
                    name_parts = name.split('.')
                    first_name = name_parts[0].capitalize()
                    last_name = name_parts[-1].capitalize()
                    result.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'status': item['status'],
                        'type': item['type']
                    })
            elif item['type'] == 'phone':
                phone = item['phone']
                if phone.startswith('+1'):
                    area_code = phone[2:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+44'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+33'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+49'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+41'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+39'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+31'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+43'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+34'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
                elif phone.startswith('+32'):
                    area_code = phone[3:5]
                    prefix = phone[5:8]
                    line_number = phone[8:]
                    result.append({
                        'area_code': area_code,
                        'prefix': prefix,
                        'line_number': line_number,
                        'status': item['status'],
                        'type': item['type']
                    })
    return result
