import json
import random

def generate_scores():
    # Generate a random score for the output key
    data = {
        'output': random.randint(0, 100),
        'subscore1': random.randint(0, 100),
        'subscore2': random.randint(0, 100)
    }
    return data

def write_to_json(data, filename="output.json"):
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    scores = generate_scores()
    
    # Write scores to output.json
    write_to_json(scores)
    
    # Print scores for summary
    print("Summary of scores:")
    for key, value in scores.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
