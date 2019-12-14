#!/usr/bin/env python3


def main(input_string, command_declarative, append_character, max_characters):
    string_prefix = ''
    # identify if the original string begins with a command_declarative, which will be placed at the beginning of
    # all subsequent text commands
    if str(input_string).startswith(command_declarative):
        import re
        pattern_matches = re.findall('([^\\s]+)', input_string)
        if pattern_matches:
            string_prefix = pattern_matches[0]

    raw_data = str(input_string).split()
    results = []
    sub_results = []
    for i in range(len(raw_data)):
        # if the new word plus the existing blocks plus the append character are greater than or equal to he max
        # characters, append the current group-as is and reset for a new subgroup
        if (len(raw_data[i]) + 1) + len(' '.join(sub_results)) + (len(string_prefix) + 1) + len(append_character) > max_characters:
            # add the current block of words as a string to the results list
            if sub_results[0] == string_prefix:
                results.append(f'{" ".join(sub_results)}{append_character}'.strip())
            else:
                results.append(f'{string_prefix} {" ".join(sub_results)}{append_character}'.strip())

            # reset the sub_results
            sub_results.clear()
            sub_results.append(raw_data[i])

        else:
            # there's plenty of room to add the next word block
            sub_results.append(raw_data[i])

    # append the final block to the results
    results.append(f'{string_prefix} {" ".join(sub_results)}'.strip())

    # integrated test that all results will be equal to or below the max_characters
    for r in results:
        assert len(r) <= max_characters

    return results


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='String to break into constituent pieces')
    parser.add_argument('-m', '--max-characters', default=200, type=int, help='Maximum characters per string')
    parser.add_argument('-e', '--command-declarative', default='/',
                        help='Indicates a character which informs the game textbox that what follows is a command, '
                             'such as "/" for emote')
    parser.add_argument('-a', '--append-character', default='+',
                        help='Set the character which should be appended to strings which continue beyond the '
                             'max-characters value')
    parser.add_argument('--version', action='version', version='20191213')

    args = parser.parse_args()

    output = main(input_string=args.input,
                  command_declarative=args.command_declarative,
                  append_character=args.append_character,
                  max_characters=args.max_characters)

    # prints and empty line to keep things clean between the command and output
    print()
    for line in output:
        print(line)
