from crud_business import valid_date, get_id
from domain import PackageList, Package


def activate_command_line_menu(package_list):

    print("Command line menu activated! Enter commands: \n")
    batch = []
    command = input()
    batch.append(command)
    while command != "-e":
        command = input()
        batch.append(command)

    parse_commands(package_list, batch)


def parse_commands(package_list, batch):
    for command in batch:
        parse(package_list, command)

# add start_date finish_date destination price
# add 20/11/2026 30/11/2026 paris 2500

def parse(package_list, command):
    arguments = command.split()
    output_messages = []
    match arguments[0]:
        case "add":
            output = add_with_command(package_list, arguments)
            if output: output_messages.append(output)
        case "mod":
            output = modify_with_command(package_list, arguments)
            if output: output_messages.append(output)
        case "del": delete_with_command(package_list, arguments)
        case "print-list": output_messages.append(package_list.get_package_list())
        case "print-history": output_messages.append(package_list.get_package_list_history())
        case "-e": exit()
        case _: output_messages.append(f"Invalid command: '{" ".join(arguments)}'")

    if output_messages:
        output_messages = [str(output) for output in output_messages]
        print("Output:")
        print("\n".join(output_messages))

def add_with_command(package_list, arguments):

    if not arguments:
        return None

    if len(arguments) != 5:
         return f"Invalid number of arguments for instruction '{" ".join(arguments)}'"

    arguments = arguments[1:]
    candidate = {
        "start_date": "",
        "finish_date": "",
        "destination": "",
        "price": 0
    }
    output_message = []
    for i in range(len(arguments)):
        match i:
            case 0:
                condition, feedback = valid_date(arguments[i])
                if condition:
                    candidate["start_date"] = arguments[i]
                else:
                    output_message.append(feedback)
                    return "\n".join(output_message)
            case 1:
                condition, feedback = valid_date(arguments[i], candidate["finish_date"])
                if condition and candidate["start_date"]:
                    candidate["finish_date"] = arguments[i]
                else:
                    output_message.append(feedback)
                    return "\n".join(output_message)
            case 2:
                candidate["destination"] = arguments[i]
            case 3:
                if arguments[i].isdigit():
                    candidate["price"] = int(arguments[i])
                else:
                    output_message.append("The package price must be a digit")
                    return "\n".join(output_message)

    new_package = Package(candidate["start_date"], candidate["finish_date"], candidate["destination"], candidate["price"],get_id())
    package_list.add_package(new_package)
    return "\n".join(output_message)

# mod id attribute value
# mod 10395925 start_date 04/12/2026

def modify_with_command(package_list, arguments):
    if not arguments:
        return None

    if len(arguments) != 4:
         return f"Invalid number of arguments for instruction '{" ".join(arguments)}'"

    condition, index = package_list.exists_id(arguments[1])
    if not condition:
        return "The id doesn't exist"

    selected_package = package_list.get_package(arguments[1])
    new_package = ""

    match arguments[2]:
        case "start_date":
            if not valid_date(arguments[3]):
                return "The date must match the pattern dd/mm/yyyy"
            new_package = Package(arguments[3], selected_package.get_finish_date(), selected_package.get_destination(), selected_package.get_price(), selected_package.get_id())
        case "finish_date":
            if not valid_date(arguments[3]):
                return "The date must match the pattern dd/mm/yyyy"
            new_package = Package(selected_package.get_start_date(), arguments[3], selected_package.get_destination(), selected_package.get_price(), selected_package.get_id())
        case "destination":
            new_package = Package(selected_package.get_start_date(), selected_package.get_finish_date(), arguments[2], selected_package.get_price(), selected_package.get_id())
        case "price":
            if not arguments[3].isdigit():
                return "The price must be an integer"
            new_package = Package(selected_package.get_start_date(), selected_package.get_finish_date(), selected_package.get_destination(), arguments[2], selected_package.get_id())
        case _:
            return "Invalid attribute"

    package_list.get_package_list()[index] = new_package
    return ""

# del id
# del 12461346

def delete_with_command(package_list, arguments):
    if not arguments:
        return None

    if len(arguments) != 2:
        return f"Invalid number of arguments for instruction '{" ".join(arguments)}'"

    condition, index = package_list.exists_id(arguments[1])
    if not condition:
        return "The id doesn't exist"

    package_list.update_history()
    package_list.get_package_list().pop(index)
    return ""