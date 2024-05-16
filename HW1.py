import feedparser
import pprint
# Parse the RSS feed
feed1 = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Day=tomorrow')  
 
feed2 = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Day=today')

today_tomorrow = feed1['entries'] + feed2 ['entries']
 
sorted_entries = sorted(today_tomorrow ,key=lambda entry: float(entry['price']))

#pprint.pprint(today_tomorrow) 

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
    <h2>Fuel Prices</h2>
    <table>
        <tr>
            <th>day</th>
            <th>location</th>
            <th>Address</th>
            <th>Price today</th>
            <th>Brand</th>
        
        </tr>
        
"""
for entry in sorted_entries:
    day = "Tomorrow" if entry in feed1['entries'] else "Today"
    
    location = entry['location']
    address = entry['address']
    price = entry['price']
    brand = entry['brand']
    # Append row to HTML content
    html_content += f"""
        <tr>
            <td>{day}</td>
            <td>{location}</td>
            <td>{address}</td>
            <td>{price}</td>
            <td>{brand}</td>
        </tr>
    """

html_content += """    

</table>
    <table>
    <tr>
            <th>Address</th>
            <th>Price </th>
            <th>Brand</th>
        </tr>
"""

html_content += """
    </table>
</body>
</html>
"""

# Write the HTML content to a file
with open('fuel_prices3.html', 'w') as f:
    f.write(html_content)

print("HTML file created successfully.")
