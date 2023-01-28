from prompts import prompts
from run import analyze, run_report
from selections import selections as select

if __name__ == "__main__":
    print(prompts['intro'])
    selection = input()

    if selection is select['analyze']:
        analyze()
    elif selection is select['run report']:
        run_report()
    else:
        print(f'"{selection}" is not an option')