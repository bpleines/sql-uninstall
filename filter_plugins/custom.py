def service_list(string):
    serviceString = string
    flatten = serviceString.split(":")
    flatten.pop(0)
    services = []
    for element in flatten:
        serviceChars = element.split(' ', 2)
        service = serviceChars[1].split('\r',1)
        services.append(service[0])
    return services

def program_list(string):
    serviceString = string
    flatten = serviceString.split(":")
    flatten.pop(0)
    services = []
    for element in flatten:
        serviceChars, withProg = element.split(' ', 1)
        program, rest = withProg.split('\r', 1)
        services.append(program)
    return services

def admin_list(string):
    adminString = string
    before, including = adminString.split("------------------------------------------------------------------------------")
    allAccounts = including.split('\r\n')
    accountsToRemove = []
    for account in allAccounts:
        if "CommVault" in account:
            accountsToRemove.append(account)
        elif ("SQL" or "Sql") in account:
            accountsToRemove.append(account)
        else:
            pass
    return accountsToRemove

def get_drive_file(string):
    standardOut = string
    before, including = standardOut.split("Name : ", 1)
    trimmed = including.strip()
    #drive_file, rest = trimmed.split('\r', 1)
    return trimmed

class FilterModule(object):
    def filters(self):
        return {
            'service_list': service_list,
            'program_list': program_list,
            'admin_list': admin_list,
            'get_drive_file' : get_drive_file
            }
