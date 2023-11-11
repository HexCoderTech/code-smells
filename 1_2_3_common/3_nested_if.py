VALID_DOMAINS = {
    '@gmail.com',
    '@yahoo.com',
    '@hotmail.com',
    '@aol.com',
    '@outlook.com',
    '@icloud.com',
    '@protonmail.com',
    '@tutanota.com',
    '@mail.com',
    '@yandex.com',
    '@zoho.com',
    '@gmx.com',
    '@web.de',
    '@yahoo.co.uk',
    '@yahoo.ca',
    '@yahoo.de',
    '@yahoo.fr',
    '@yahoo.it',
    '@yahoo.es',
    '@yahoo.in'
}

PHONE_CODES = {
    '+1' ,
    '+44',
    '+33',
    '+49',
    '+41',
    '+39',
    '+31',
    '+43',
    '+34',
    '+32',
}

def parse_email(email):
    name, domain = email.split('@')

    if not name or not domain:
        return None

    name_parts = name.split('.')

    if len(name_parts) < 2:
        return None

    first_name = name_parts[0].capitalize()
    last_name = name_parts[-1].capitalize()
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'domain': domain,
    }

def parse_phone(phone):
    if not phone.startswith('+'):
        return None
    start = -1
    if phone.startswith('+1'):
        start = 2
    else:
        start = 3
    
    area_code = phone[start:5]
    prefix = phone[5:8]
    line_number = phone[8:]
    return{
        'area_code': area_code,
        'prefix': prefix,
        'line_number': line_number,
    }

def process_data(data):
    result = []
    for item in data:
        if item['status'] != 'active':
            continue

        if item['type'] == 'email':
            email = item['email']
            parsed_email = parse_email(email)
            
            if not parsed_email:
                continue

            element = {
                'first_name': parsed_email['first_name'],
                'last_name': parsed_email['last_name'],
                'email': email,
                'status': item['status'],
                'type': item['type']
            }
            result.append(element)
            
        elif item['type'] == 'phone':
            phone = item['phone']
            parsed_phone = parse_phone(phone)
            if not parsed_phone:
                continue
            
            result.append({
                    **parsed_phone,
                    'status': item['status'],
                    'type': item['type']
                })
    return result
