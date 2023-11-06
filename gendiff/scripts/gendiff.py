
def main():
    args = parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    output_format = args.format
    print(generate_diff(file_path1, file_path2, output_format))


if __name__ == '__main__':
    main()
