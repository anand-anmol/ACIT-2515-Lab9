# contacts_w4_ex_5.py
#
# Create and manage a list of contacts. This version of the program includes
# code for Week 3 Lab Exercise 3: addinfo and delinfo.
#
# Author: Anmol Anand - A01174846
#


def get_cmd():
    user_input = input("Enter a command: ")
    input_list = user_input.split()
    command = input_list[0]
    args = input_list[1:]
    return command, args


def add_contact(arg_list):
    new_contact = " ".join(arg_list)
    if new_contact in _contacts:
        print(new_contact, "already exists in the database")
    else:
        info = {}
        _contacts[new_contact] = info


def show_contacts():
    print(_contacts)


def delete_contact(arg_list):
    contact_to_delete = " ".join(arg_list)
    if contact_to_delete in _contacts:
        del (_contacts[contact_to_delete])
    else:
        print(contact_to_delete, "does not exist in the database")


def rename_contact(arg_list):
    contact_to_rename = " ".join(arg_list)
    if contact_to_rename in _contacts:
        new_name = input("Enter a new name for " + contact_to_rename + ": ")
        if new_name in _contacts:
            print(new_name, "already exists in the database")
        else:
            info = _contacts[contact_to_rename]
            _contacts[new_name] = info
            delete_contact(arg_list)
    else:
        print(contact_to_rename, "does not exist in the database")


def show_info(arg_list):
    contact_to_display = " ".join(arg_list)
    if contact_to_display in _contacts:
        info = _contacts[contact_to_display]
        print("%s: %s" % (contact_to_display, info))
    else:
        print(contact_to_display, "does not exist in the database")


def add_info(arg_list):
    contact_name = " ".join(arg_list)
    info_type_accepted = ('Phone', 'Cell', 'Mobile', 'Email', 'Other', 'LinkedIn')
    if contact_name in _contacts:
        info = _contacts[contact_name]
        user_input = input("Enter contact info for " + contact_name + ": ")
        user_input = user_input.strip()
        if ":" in user_input:
            info_type, info_value = user_input.split(':')
            if info_type in info_type_accepted:
                if info_type in info:
                    print(info_type, "already exists for", contact_name)
                else:
                    if info_type == 'Phone':
                        num_portion_1 = info_value[0:3]
                        num_portion_2 = info_value[4:7]
                        num_portion_3 = info_value[8:11]
                        if (len(info_value) == 12 and info_value[3] == '-' and info_value[7] == '-' and
                                num_portion_1.isdigit() and num_portion_2.isdigit() and num_portion_3.isdigit()):
                            info[info_type] = info_value
                            _contacts[contact_name] = info
                        else:
                            print("Please enter Phone info in the following format:")
                            print('nnn-nnn-nnnn')
                    elif info_type == 'Email':
                        if ('@' in info_value and '.' in info_value and info_value.count('@') == 1 and
                                info_value.count('.') == 1):
                            if info_value.index('@') < info_value.index('.'):
                                info[info_type] = info_value
                                _contacts[contact_name] = info
                            else:
                                print('Please enter Email info in the following form:')
                                print('a@b.c')
                        else:
                            print('Please enter Email info in the following form:')
                            print('a@b.c')
                    else:
                        info[info_type] = info_value
                        _contacts[contact_name] = info
            else:
                print(info_type, "is not an accepted info type.")
        else:
            print('Please enter info in the following format:')
            print('<info type>:<info value>')
    else:
        print(contact_name, "does not exist in the database")


def delete_info(arg_list):
    contact_name = " ".join(arg_list)
    if contact_name in _contacts:
        info = _contacts[contact_name]
        contact_type = input("Enter type of contact info to delete: ")
        if contact_type in info:
            del (info[contact_type])
        else:
            print(contact_type, "not available for", contact_name)
    else:
        print(contact_name, "does not exist in the database")


def invalid_input():
    print('Unknown command: ', cmd)
    print('Valid commands are: add, delete, rename, info, show, addinfo, delinfo, quit')


if __name__ == "__main__":

    _contacts = {}
    cmd, args = get_cmd()
    while cmd != 'quit' and cmd != 'q':

        if cmd == 'add':
            add_contact(args)
        elif cmd == 'show':
            show_contacts()
        elif cmd == 'delete' or cmd == 'del':
            delete_contact(args)
        elif cmd == 'rename' or cmd == 'ren':
            rename_contact(args)
        elif cmd == 'info' or cmd == 'showinfo':
            show_info(args)
        elif cmd == 'addinfo':
            add_info(args)
        elif cmd == 'delinfo':
            delete_info(args)
        else:
            invalid_input()

        cmd, args = get_cmd()

    exit()
