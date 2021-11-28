import os, tarfile, re, time, json

# global wordDict
globalWordDict = {}
fileWordDict = {}
stopList = {"a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"}
MEDIA_ROOT = os.curdir+'/upload'

# Utility Methods
def buildIndex(filename):
    start_time = time.time()
    # print("##### Build Index ######")

    # creat a folder for indexes if it doesn't exist
    indexDirPath = os.curdir + "/index"
    if not os.path.exists(indexDirPath):
        # Create a new directory because it does not exist 
        os.makedirs(indexDirPath)

    # Parse the file and conctruct a dict
    # print(MEDIA_ROOT)
    # print("Media Dir: " + MEDIA_ROOT)
    
    # Store the unzipped file in a tmp directory
    dirPath= MEDIA_ROOT + "/extracted/" + filename
    # print("File Path: " + dirPath)
    
    # Unzip a tar.gz file
    zipPath = MEDIA_ROOT + "/" + filename
    # print("Zipfile Path: " + zipPath)
    zipFile = tarfile.open(zipPath)
    zipFile.extractall(dirPath)
    zipFile.close()
    # print("Unzipping file success")

    # Read files from the extracted directory recursively
    rootDir = dirPath
    
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            # read files and build indexes
            filePath = os.path.join(root, file)
            # print("File Path: " + filePath)
            with open(filePath, 'r', encoding="ISO-8859-1") as file:
                wordDict = {}

                # creat new dict for new fileName/filePath
                if filePath not in fileWordDict:
                    fileWordDict[filePath] = {}

                wordDict = fileWordDict[filePath]
                
                for line in file:
                    # split by whitespace on every line
                    # and store words and its frequency in a dict
                    words = line.strip().split()
                    for rawWord in words:
                        # strip non-alphanum chars
                        word = re.sub(r'\W+', '', rawWord.lower())
                        if word in stopList:
                            continue
                        
                        if word not in wordDict:
                            wordDict[word] = 0
                        wordDict[word] += 1

                        if word not in globalWordDict:
                            globalWordDict[word] = 0
                        globalWordDict[word] += 1
                    
            # Print the dict for debugging
            # print("##### Printing File Word Dict ######")

            # write hashmaps to presistent files
            # convert '/' to '#' in filepath
            # print(file.name)
            fileIdxPath = indexDirPath + '/' + os.path.relpath(file.name).lstrip('upload/extracted/').replace('/', '#')
            # print(fileIdxPath)
            with open(fileIdxPath, 'w') as write_file:
                write_file.write(json.dumps(wordDict))

            # sort_wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
        
            # cnt = 0
            # for entry in sort_wordDict:
            #     if cnt > 20:
            #         break
            #     # print("Word: "+entry[0]+", freq: "+str(entry[1]))
            #     cnt += 1

    # Print the dict for debugging
    # print("##### Printing Global Word Dict ######")

    # sort_wordDict = sorted(globalWordDict.items(), key=lambda x: x[1], reverse=True)

    # cnt = 0
    # for entry in sort_wordDict:
    #     if cnt > 20:
    #         break
    #     print("Word: "+entry[0]+", freq: "+str(entry[1]))
    #     cnt += 1


    # write hashmaps to presistent files
    with open(indexDirPath + '/globalIndex', 'w') as write_file:
        write_file.write(json.dumps(globalWordDict))
    
    
    end_time = time.time()

    execTime = end_time-start_time

    print(execTime)

    return execTime