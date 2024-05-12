

import random

def generate_list_imdb(filename):
    titles_list = []
    year_list = []
    certificate_list = []
    genre_list = []
    details_list = []
    actor_list = []
    earning_list = []
    ##**edited**##
    rating_list = []
    ##**##
    
    file_in = open(filename)
    file_in.readline()

    for line in file_in:
        line = line.strip().split(",")
        
        titles_list.append(line[0])
        year_list.append(int(line[1]))
        certificate_list.append(line[2])
        genre_list.append(line[3])
        details_list.append(line[4])
        actor_list.append(line[5])
        earning_list.append(float(line[6]))
        rating_list.append("")
        
    return titles_list, \
            year_list, \
            certificate_list, \
            genre_list, \
            details_list, \
            actor_list, \
            earning_list, \
            rating_list

def print_menu(menu_list, program_title):

    print("\n"*5)
    print(program_title)
    print('*'*len(program_title))
    for i in range(0, len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')


def get_menu_selection(menu_list):

    possible_choice_values = []
    for i in range(0, len(menu_list)):
        possible_choice_values.append(str(i+1))

    choice = input("Type number to choose ... ")

    while choice not in possible_choice_values:
        print("Incorrect selection")
        print("\n"*30)
        
        print_menu(menu_list,"")
        choice = input("Type number to choose ...")

    return int(choice)

def get_unique_info(list_of_all_info):
    unique_info = []
    for item in list_of_all_info:
        if str(item) not in unique_info:
            unique_info.append(str(item))

    unique_info.sort()

    return unique_info

def get_unique_int(list_of_all_int):
    unique_int = []
    for item in list_of_all_int:
        if int(item) not in unique_int:
            unique_int.append(int(item))

    unique_int.sort()

    return unique_int
    
##**##

def print_genres(list_unique_genres):
    print("\n\nAll genres available are:")
    print("-"*20)
    for i in range(0, len(list_unique_genres)):
        print(f'{list_unique_genres[i]:<30}')
    
    print("\n")


def get_valid_genre(list_unique_genres):
    user_genre_choice = input("What genre would you like to filter for?")
    while user_genre_choice not in list_unique_genres:
        user_genre_choice = input("Sorry that league is not valid. Please try again")
    
    return user_genre_choice

##**used again**##
def get_valid_listing(list_of_indexes):
    possible_choice_values = []
    

    for i in range(0, len(list_of_indexes)):
        possible_choice_values.append(str(i+1))
        
    if len(list_of_indexes) > 1:
        print("*"*40)
        choice = input("\nWhich listing number would you like to choose?")
        while choice not in (possible_choice_values):
            choice = input("\nInvalid choice. Try another number")

        choice = int(choice) - 1

    else:
        choice = 0

    return list_of_indexes[choice]

##**##

def filter_all_listings(genre_list, current_genre):
    matched_indexes = []

    for i in range(0, len(genre_list)):
        if genre_list[i] == current_genre:
            matched_indexes.append(i)

    return matched_indexes


##**used again**##
def print_listings_by_index(list_imdb_indexes, current_genre, titles_list, year_list):

    print("\nSelected Movies:")
    for i in range(0, len(list_imdb_indexes)):
        imdb_index = list_imdb_indexes[i]
        title = titles_list[imdb_index]
        year = year_list[imdb_index]
        
        s = f'{i+1:<3} {title[0:48]:<50} {year} {current_genre}'
        print(s)

##**##

def print_single_imdb_details(current_index, genre_list, titles_list, year_list, certificate_list, details_list, actor_list, earning_list, all_rating_list):

    genre = genre_list[current_index]
    title = titles_list[current_index]
    year = year_list[current_index]
    certificate = certificate_list[current_index]
    details = details_list[current_index]
    actor = actor_list[current_index]
    earnings = earning_list[current_index]
    rating = all_rating_list[current_index]

    print("*"*40)
    print("\nMovie information:")
    print(f'{"Title:":<12} {title}')
    print(f'{"Year:":<12} {year}')
    print(f'{"Genre:":<12} {genre}')
    print(f'{"Certificate:":<12} {certificate}')
    print(f'{"Details:":<12} {details[0:60]}...')
    print(f'{"Actor:":<12} {actor}')
    print(f'{"Earnings:":<12} {earnings}')
    if rating != "":
        print(f'{"Rating:":<12} {rating}/10')
    else:
        pass

    
def print_listings(titles_list, year_list, certificate_list, genre_list, details_list, actor_list, earning_list, all_rating_list):

    print("\n\nAll IMDB Listings")
    for i in range(0, 10):
        print(titles_list[i], year_list[i], certificate_list[i])

###YOU WILL ADD YOUR ADDITIONAL FUNCTIONS HERE
##MENU OPTION NUMBER 3
        
def print_years(list_unique_years):
    print("\n\nAll years available are:")
    print("-"*20)
    for i in range(0, len(list_unique_years)):
        print(f'{list_unique_years[i]:<30}')
    
    print("\n")


def get_valid_year(list_unique_years):
    user_year_choice_low = input("What is the lower number of the year range?")
    check_low_year = user_year_choice_low.isdigit()
    
    while check_low_year == False:
        print("\nSorry that year is not valid. Please try again")
        user_year_choice_low = input("What is the lower number of the year range?")
        check_low_year = user_year_choice_low.isdigit()

    user_year_choice_high = input("\nWhat is the higher number of the year range?")
    check_high_year = user_year_choice_high.isdigit()

    while check_high_year == False or user_year_choice_high < user_year_choice_low:
        print("\nSorry that year is not valid. Please try again")
        user_year_choice_high = input("What is the higher number of the year range?")
        check_high_year = user_year_choice_high.isdigit()

    return user_year_choice_low, user_year_choice_high

def filter_all_listings_year(year_list, low_year, high_year):
    matched_indexes = []
    ly = int(low_year)
    hy = int(high_year)

    for i in range(0, len(year_list)):
        if year_list[i] >= ly and year_list[i] <= hy:
            matched_indexes.append(i)

    return matched_indexes

def print_current_imbd(current_index, title_list, actor_list):
    title = title_list[current_index]
    actor = actor_list[current_index]

    print("*"*40)
    print('\nThe movie seleted:')
    print(f'Title: {title}')
    print(f'Actor: {actor}')
    
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def get_valid_rating(current_index, rating_list):
    #possible_rating = ["0","1","2","3","4","5","6","7","8","9","10"]
    current_rating = input("What rating would you like to give? (A mark out of 10, over 10 means extrodinary)")
    check_int_rating = current_rating.isdigit()
    check_float_rating = isfloat(current_rating)
    print(check_int_rating, check_float_rating)
    
    while check_int_rating == False and check_float_rating == False:
        print("Sorry that was an invalid rating, try again.")
        current_rating = input("What rating would you like to give? (A mark out of 10)")
        check_int_rating = current_rating.isdigit()
        check_float_rating = isfloat(current_rating)
        print(check_int_rating, check_float_rating)
        
    rating_list[current_index] = current_rating
    #return current_rating


##MENU OPTION NUMBER 4
def print_titles(list_unique_title):
    print("\n\nAll movies available are:")
    print("-"*20)
    for i in range(0, len(list_unique_title)):
        print(f'{list_unique_title[i]:<30}')
    
    print("\n")
    
def filter_valid_title(title_list):
    print("")
    print("*"*40)
    matched_indexes = []
    user_text = input("Search for your desired movie keyword:")
    print("")

    for i in range(0, len(title_list)):

        if user_text in title_list[i]:
            
            matched_indexes.append(i)


    if matched_indexes == []:
        print("Sorry, that title is not valid. A random title will be selected for you:")
        random_user = random.randrange(0,len(title_list))
        matched_indexes.append(random_user)

    return matched_indexes

def get_valid_actor(current_index, all_actor):
    
    new_actor = input("\nWho would you like to change the lead actor into? ")
    all_actor[current_index] = new_actor
    

def print_titles_by_index(list_imdb_indexes, titles_list, actor_list):

    print("\nSelected Movies:")
    print(f'{"#":<3} {"Title":<50} {"Actor"}')
    print("-"*70)
    for i in range(0, len(list_imdb_indexes)):
        imdb_index = list_imdb_indexes[i]
        title = titles_list[imdb_index]
        actor = actor_list[imdb_index]
        
        s = f'{i+1:<3} {title[0:48]:<50} {actor}'
        print(s)     
    
def main():
    program_title = "IMDB Movie & Series Listings"

    all_titles_list, \
        all_year_list, \
        all_certificate_list, \
        all_genre_list, \
        all_details_list, \
        all_actor_list, \
        all_earning_list, \
        all_rating_list = generate_list_imdb("imdb_listings.csv")

    all_genres = get_unique_info(all_genre_list)
    all_years = get_unique_int(all_year_list)
    all_titles = get_unique_info(all_titles_list)

    menu_items = ['See All IMDB Listings', 'Find Listing by Genre', 'Add rating to movie by filtering by year', 'Change lead actor name', 'TBD', 'Exit']

    print_menu(menu_items, program_title)
    choice = get_menu_selection(menu_items)
    
    while choice != len(menu_items):

        ##See all listings
        if choice == 1:
            print_listings(all_titles_list, \
                            all_year_list, \
                            all_certificate_list, \
                            all_genre_list, \
                            all_details_list, \
                            all_actor_list, \
                            all_earning_list, \
                            all_rating_list)
    

        #Find listing by Genre
        elif choice == 2:
            print_genres(all_genres)
            current_genre = get_valid_genre(all_genres)

            list_imdb_indexes = filter_all_listings(all_genre_list, current_genre)
            print("testing", list_imdb_indexes)
            print_listings_by_index(list_imdb_indexes, current_genre, all_titles_list, all_year_list)
            current_imdb_index = get_valid_listing(list_imdb_indexes)

            print_single_imdb_details(current_imdb_index , \
                                            all_genre_list, \
                                            all_titles_list, \
                                            all_year_list, \
                                            all_certificate_list, \
                                            all_details_list, \
                                            all_actor_list, \
                                            all_earning_list, \
                                            all_rating_list)
            
        #Add rating to movie by filtering by year  
        elif choice == 3:
            print_years(all_years)
            current_low_year, current_high_year = get_valid_year(all_years) 

            list_imdb_indexes_year = filter_all_listings_year(all_year_list, current_low_year, current_high_year)
            print_listings_by_index(list_imdb_indexes_year, "", all_titles_list, all_actor_list)
            current_imdb_index_year = get_valid_listing(list_imdb_indexes_year)

            print_current_imbd(current_imdb_index_year, all_titles_list, all_actor_list)
            get_valid_rating(current_imdb_index_year, all_rating_list)
            print_single_imdb_details(current_imdb_index_year , \
                                            all_genre_list, \
                                            all_titles_list, \
                                            all_year_list, \
                                            all_certificate_list, \
                                            all_details_list, \
                                            all_actor_list, \
                                            all_earning_list, \
                                            all_rating_list)
        #Change lead actor name by searching through movie keyword 
        elif choice == 4:
            imbd_index_title = filter_valid_title(all_titles_list)

            print_titles_by_index(imbd_index_title, all_titles_list, all_actor_list) 
            current_imbd_index_title = get_valid_listing(imbd_index_title)
            print_current_imbd(current_imbd_index_title, all_titles_list, all_actor_list)

            get_valid_actor(current_imbd_index_title, all_actor_list)
            print_single_imdb_details(current_imbd_index_title , \
                                            all_genre_list, \
                                            all_titles_list, \
                                            all_year_list, \
                                            all_certificate_list, \
                                            all_details_list, \
                                            all_actor_list, \
                                            all_earning_list, \
                                            all_rating_list)

        elif choice == 5:
            pass
##            index = int(input("Type index"))
##            print_single_imdb_details(index , \
##                                            all_genre_list, \
##                                            all_titles_list, \
##                                            all_year_list, \
##                                            all_certificate_list, \
##                                            all_details_list, \
##                                            all_actor_list, \
##                                            all_earning_list, \
##                                            all_rating_list)
            
            

        print_menu(menu_items, program_title)
        choice = get_menu_selection(menu_items)
        

    print("\n\nGoodbye! Enjoy Reading.")
    

    
#NO CODE IS ADDED AFTER THIS POINT    
main()

