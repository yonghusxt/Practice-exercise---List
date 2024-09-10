
string_list = list()
num_list = list()
i=0
while i < 9:
    name=input("please enter the name:")
    score=input("please enter the score:")
    if score.isdigit():
        score=int(score)
        if score>=0 and score<=5:
            string_list.append(name)
            num_list.append(score)
            i=i+1
        else:
            print("Please enter a number between 0-5.")
    else:
        print("please enter a number.")
        continue
   

paired_list = list(zip(num_list,string_list))
print(paired_list)
while True:
    print("1.View the student with the highest grade")
    print("2.View top three students with the highest grade")
    print("3.View the students with the lowest grade")
    print("4.Get the total number of students that failed")
    print("5.Exit.")
    print("------------------------------------------------------")
    choose = input("Please select the option you want to view:")
    if choose.isdigit():
        choose = int(choose)
        if choose == 5:
          print("Exit.")
          break
        elif choose == 1:
          list1 = sorted(paired_list, reverse = True)
          print(f"The highest grade student: {list1[0]}")
          continue
        elif choose == 2:
          list1 = sorted(paired_list, reverse = True)
          top_three_list = list1[:3]
          print("The top three students with the highest grade:")
          for num, str in top_three_list:
             print(f'{str},{num}')
          continue
        elif choose == 3:
          list1 = sorted(paired_list, reverse = True)
          print(f"The lowest grade student: {list1[-1]}")
          continue
        elif choose == 4:
          list1 = sorted(paired_list, reverse = True)
          for num, str in list1:
             if num == 0:
                print(f'{str},{num}')
          continue
        else:
          print("Please enter the correct number.")
          continue
    else:
        print("Please enter the correct numberd.")
        continue
         

