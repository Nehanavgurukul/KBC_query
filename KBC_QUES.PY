question_list = [
    "How many continents are there?",           
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"   
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]


solution_list = [3, 4, 1]


index1=0
a=0
while(index1<len(question_list)):
    print((index1+1),".",question_list[index1])
    
    user_ans=int(input("enter the user ans number"))
    
    if(user_ans == a):
        print("aap already life line use kar  chuke ho")
        break
    elif (user_ans==solution_list[index1] or user_ans==5050):
        if(user_ans==solution_list[index1]):
            print("apka ans sahi  right h")
        else:
            if(user_ans==5050):
                user_ans=int(input("enter the user ans number"))
                if(user_ans==solution_list[index1]):
                    print("apka ans sahi hai ")
                    a=a+user_ans
                else:
                    print("apke paas ek option or hai jabab dene ke liye ")
                    user_ans=int(input("enter the user ans number"))
                    if(user_ans==solution_list[index1]):
                        print("aapka ans sahi hai")
                        a=a+user_ans


    else:
        print("sorry apka ans wrong h")
        break

    index1=index1+1

