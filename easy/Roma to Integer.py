def romanToInt( s: str) -> int:
        # define dict
        # better than best solution on leet code ( same for test case with no substraction)
        # more space complextity

        my_dict ={
            "I": 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" :40,
            "L": 50,
            "XC" : 90,
            "C" :100,
            "CD" :400,
            "D":500,
            "CM": 900,
            "M":1000
            
        }
        sum =0
        # two counter check for substraction
        first_index =0
        last_index =2
        while last_index<= (len(s)+1):
            # check for substraction
            if(s[first_index:last_index] in my_dict):
                sum+= my_dict[s[first_index:last_index]]
                first_index =last_index
                last_index +=2
            # check for single value
            elif(s[first_index:last_index-1] in my_dict):
                sum+= my_dict[s[first_index:last_index-1]]
                first_index =last_index-1
                last_index+=1
            
        return sum
print(romanToInt("MCMXCIV"))
            
