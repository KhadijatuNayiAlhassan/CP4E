from mustaph_class import WashMachine
def main():
    water_temp= eval(input("please enter the water type for washing, ie 0 for hot or 1 for cold:"))
    cloth_weight = eval(input("please enter the weight of the clothes in grams.eg 1000 if 1kg :"))
    a = WashMachine(water_temp,cloth_weight)
main()