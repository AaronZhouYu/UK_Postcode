#!/usr/bin/python3

import sys
import json
import inquirer
import requests

def loadJsonStatus(url):
    return requests.get(url).json()['status']

def loadJsonResult(url):
    return requests.get(url).json()['result']

def loadJsonError(url):
    return requests.get(url).json()['error']

def lookupPostcode(postcode):
    url = 'https://api.postcodes.io/postcodes/{}'.format(postcode)
    return loadJsonResult(url)

def queryPostcode(postcode):
    url = 'https://api.postcodes.io/postcodes?q={}'.format(postcode)
    return loadJsonResult(url)

def validatePostcode(postcode):
    url = 'https://api.postcodes.io/postcodes/{}/validate'.format(postcode)
    return loadJsonResult(url)

def nearestPostcode(postcode):
    url = 'https://api.postcodes.io/postcodes/{}/nearest'.format(postcode)
    return loadJsonResult(url)

def validate(postcode):
    validate_url = 'https://api.postcodes.io/postcodes/{}/validate'.format(postcode)
    # validate the postcode
    validate_status = requests.get(validate_url).json()['status']
    
    if(validate_status is 200) :
        validate_result = requests.get(validate_url).json()['result']
        
        if (validate_result == True) :
            return postcode
        else :
            query_url = 'https://api.postcodes.io/postcodes?q={}'.format(postcode)
            # query for the postcode
            query_status = requests.get(query_url).json()['status']
            
            if (query_status is 200) :
                query_result = requests.get(query_url).json()['result']
                
                if (query_result == None) :
                    print("The Postcode is an inappropriate value, please double check, Thanks.")
                    return False
                else :
                    value = []
                    for val in query_result :
                        value.append(val['postcode'])
                    #Generate a list of postcodes based on the postcode query results
                    questions = [
                    inquirer.List('postcode_selected', message="We have found a list of postcodes based on your input, please select the correct one",
                        carousel=True, choices = value)
                    ]
                    answers = inquirer.prompt(questions)
                    postcode = answers["postcode_selected"]
                    return postcode
            
            else :
                query_error = requests.get(query_url).json()['error']
                print(query_error)
                return False
    
    else :
        validate_error = requests.get(validate_url).json()['error']
        print(validate_error)
        return False

def main():
    args = sys.argv[1:]
    if (len(args) == 1) :
        postcode = args[0]
        #Validate the Postcode
        postcode = validate(postcode)
        
        if(postcode) :
            lookup_result = lookupPostcode(postcode)
            print("Country and Region from the Postcode:")
            print("\tPostcode: %s, \tCountry: %s, \tRegion: %s.\n" % ((lookup_result['postcode'], lookup_result['country'], lookup_result['region'])))
            nearest_result = nearestPostcode(postcode)
            print("Countries and Regions from the Nearest Postcodes:")
            for val in nearest_result :
                print("\tPostcode: %s, \tCountry: %s, \tRegion: %s." % ((val['postcode'], val['country'], val['region'])))
    
    elif (len(args) == 0) :
        print("Error: This is no argument given to the command. You have to give only one argument.")
        print("Please use any postcode with \"\" as the argument, Thanks.")
    
    else :
        print("Error: This are too many arguments given to the command. You have to give only one argument.")
        print("Please use any postcode with \"\" as the argument, Thanks.")

if __name__ == "__main__" :
    main()
