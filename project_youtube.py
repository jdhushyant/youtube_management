import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def List_all_videos(videos):
    print("\n")
    print('*' * 60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duraction: {video['time']}")
    print('*' * 60)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    List_all_videos(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new videop name : ")
        time = input("Enter the new videop time : ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    List_all_videos(videos)
    index = int(input("Entert the video number to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube manager | choose an option ")
        print("1. List all youtube video : ")
        print("2. Add a youtube video : ")
        print("3 Update a youtube video details : ")
        print("4 Delete a youtube video details : ")
        print("5 Exit the app ")
        choice = input("Enter your choice : ")

        match choice:
            case '1':
                List_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

