def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    
    # Get the list of floats from the user
    num_list = get_user_input()
    
    # Calculate average, min, and max
    average = calc_average_temperature(num_list)
    min_max_list = calc_min_max_temperature(num_list)
    
    # Display the results
    print("The average temperature is: " + str(average))
    print("The minimum and maximum temperatures are: " + str(min_max_list))