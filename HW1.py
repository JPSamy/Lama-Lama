import feedparser
import pprint
# Parse the RSS feed
feed1 = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=maddington&Day=today')

feed2 = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=maddington&Day=tomorrow')


 
#pprint.pprint(feed1)
#pprint.pprint(feed2)
# Begin HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="    " content="width=device-width, initial-scale=1.0">
    <title>Fuel Prices</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 6px;
        }
        th {
            background-color: #58cc84;
        }
    </style>
</head>
<body>
    <h2>Fuel Prices in Maddington Today</h2>
    <table>
        <tr>
            <th>Address</th>
            <th>Price today</th>
            <th>Brand</th>
        </tr>
"""

# Loop through each entry and add rows to the table
for entry in feed1['entries']:
    address = entry['address']
    price = entry['price']
    brand = entry['brand']
    # Append row to HTML content
    html_content += f"""
        <tr>
            <td>{address}</td>
            <td>{price}</td>
            <td>{brand}</td>
        </tr>
    """

html_content += """    </table>
    <table>
    <tr>
            <th>Address</th>
            <th>Price tomorrow</th>
            <th>Brand</th>
        </tr>
"""

# Loop through each entry and add rows to the table
for entry in feed2['entries']:
    address = entry['address']
    price = entry['price']
    brand = entry['brand']
    # Append row to HTML content
    html_content += f"""
        <tr>
            <td>{address}</td>
            <td>{price}</td>
            <td>{brand}</td>
        </tr>
    """

# End HTML content
html_content += """
    </table>
</body>
</html>
"""

# Write the HTML content to a file
with open('fuel_prices1.html', 'w') as f:
    f.write(html_content)

print("HTML file created successfully.")
