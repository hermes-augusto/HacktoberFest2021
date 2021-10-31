########b Datacamp Python streamline exemples ###############


# Create dictionary to query API for cafes in NYC
parameters = {'term':"cafe",
          	  'location':"NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                parameters["term"],
                parameters["location"])

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
------------------------------------------------------------------

# Create dictionary to query API for cafes in NYC
parameters = {"term": "cafe",
          	  "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                        headers=headers, 
                        params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
#=======================================================================
# Create data frame of next 500 rows with labeled columns

vt_data_first500 = pd.read_csv("vt_tax_data_2016.csv",
                       		  skiprows=0,
							  nrows=500
							  )
cols= list(vt_data_first500.head())

vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv",
							  names=cols,
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None
							  )

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())


###new
printo rint


