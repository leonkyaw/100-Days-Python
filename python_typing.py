# age: int
# name: str
# height: float
# is_human: bool
# age = 'twelve'   # this will be error, it expect an int

def police_check(age: int) -> bool:
    if age > 10:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check('twelve'):  # it is expect integer but input string
    print("You may pass")
else:
    print("Pay a fine")
