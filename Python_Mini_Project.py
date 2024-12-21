#Project Name:- Common Friends Finder

def main():
   #Dictionary to store user friends
    user_friends = {}

   #input user data
    n = int(input("Enter the number of users: "))
    for _ in range(n):
        user = input("Enter user name: ")
        friends = input(f"Enter friends of {user} (comma-separated): ").split(",")
        user_friends[user] = set(friend.strip() for friend in friends)

   #Display users and their friends 
    print("\nUser data:")
    for user, friends in user_friends.items():
        print(f"{user}: {friends}")

   #Calculating interections and unions
    print("\nMenu:")
    print("1. Find all friends (Union)")
    print("2. Find common friends among all users (Intersection)")
    print("3. Find mutual friends between two users")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        all_friends = set().union(*user_friends.values())
        print(f"All friends (Union): {all_friends}")
    elif choice == 2:
        common_friends = set.intersection(*user_friends.values())
        print(f"Common friends (Intersection): {common_friends}")
    elif choice == 3:
        user1 = input("Enter the first user: ")
        user2 = input("Enter the second user: ")
        if user1 in user_friends and user2 in user_friends:
            mutual_friends = user_friends[user1].intersection(user_friends[user2])
            print(f"Mutual friends between {user1} and {user2}: {mutual_friends}")
        else:
            print("One or both users not found.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
