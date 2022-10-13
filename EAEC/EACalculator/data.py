data = (actions, charities)

actions = {1:('Think green', 'Pack a water bottle', 'Use public transport','Take local trips',
'Switch off computers', 'Raise awareness', 'Reduce, reuse, recycle', 'Cycle to work',
'Turn off the lights','Use less water'),2:('Change your diet','Go digital',
'Eliminate single-use plastic','Compost',), 3:('Insulate your home', 'Switch to renewables', 
'Buy energy efficient', 'Use local food','Fly direct'), 4:('Offset your carbon')}

action_description = {'Think green': 'No matter how far you travel, you can take an environmentally friendly approach when you reach your destination. As well as choosing green accommodation and ethical destinations, you can also think about the tours and attractions you take. Try and walk, cycle, or use public transport, eat local food, and leave as light a carbon footprint as possible.',
'Pack a water bottle':'Although you often can`t take liquids in your carry-on luggage, you can pack a water bottle on anything you`re checking-in. Having a reusable container for your water means you can cut down on one-use plastic bottles. This can cut your carbon footprint for the manufacture and transport of each bottle. ',
'Use public transport':'Petrol cars and taxis tend to emit a lot of carbon dioxide per kilometre of travel. These greenhouse gas emissions are usually only spilt between a few people, making it quite an energy-intense way to get around. Public transport such as trains, busses, and coaches carry many people and are often more sustainable forms of travel. ',
'Take local trips': 'Sticking with the theme of your surrounding area, try and work towards field trips that are nearby. Instead of going to far-flung destinations that require planes, trains, or busses, stick to something close by. Your emissions will be far lower, and you`ll contribute to your community. ',
'Switch off computers':'An IT lab with rows of idling computers takes up a lot of energy. You can reduce your school`s energy bills and carbon footprint by keeping electronic devices turned off and unplugged when they`re not in use. ',
'Raise awareness':'Your school community might not know much about things like greenhouse gases, carbon footprints, or climate change. You can change that by raising awareness of these issues. Things like school projects and fundraising events can help to educate students and their families about the importance of protecting the environment. This can help those around you to reduce their footprints. ',
'Reduce, reuse, recycle':'Companies of all sizes use a host of different products in their day-to-day running. Whether it`s things like paper, electronic devices, packaging, or water, it all has a carbon footprint. By reducing the amount of waste you generate, reusing IT equipment, and recycling waste, you can make a real difference.',
'Cycle to work':'Cycling and walking are two of the most environmentally friendly ways to travel. And, not only are they good for the planet, but they`re also good for your health. If you can, choose to cycle or walk to work where possible. Your employer might even have a scheme that can help you purchase a bike.',
'Turn off the lights':'Powering empty rooms and office space is a huge energy drain. By making sure you turn off lights and appliances when they`re not in use, you can make sure you`re not wasting power. You could also request to install automatic, movement-sensing lights and energy-saving LED bulbs to address the issue',
'Use less water':'It takes energy and resources to process and deliver water to our homes. What`s more, it`s also quite energy-intensive to heat it once it`s there. So, by using less, you can help the environment and lower your carbon footprint. Try turning off the taps when brushing your teeth, having short showers rather than baths, and only boiling the water you need.',
'Change your diet':'The food we eat can have a significant impact on the environment. For example, meat and dairy products require a lot of land, water and energy to produce. They also create a lot of methane, a greenhouse gas. What`s more, food shipped from overseas uses a lot more resources than local produce. By eating fewer animal products, especially red meat, (or choosing a plant-based diet) and shopping for locally sourced food, you can make a big difference.  Why not support your local farmers` market?',
'Go digital':'It`s never been easier to collaborate with others online. Whether through sharing documents using cloud storage or video conferencing instead of travelling, you can reduce your waste and emissions. Try moving away from printed documents where possible, and encourage others to work on their digital skills for the workplace.',
'Eliminate single-use plastic':'Single-use plastics may be convenient, yet they`re fairly dreadful for the environment. Not only do they pollute our waterways and oceans, but they also require energy to produce and recycle. You can stop using things like disposable coffee cups and cutlery to reduce your company`s carbon footprint.',
'Compost':'Composting is surprisingly good for the environment, particularly when food waste is such a big issue. By setting up a composting scheme at your school, you can help to reduce landfill methane emissions. What`s more, this type of compost is free, doesn`t use energy to produce, and is good for your school gardens. ',
'Insulate your home':'Heating your living space can be an expensive and energy-intensive process. By insulating places like your loft and walls, you can make sure your home retains heat during the winter and stays cool in summer. It means you`ll use less energy, reducing your carbon footprint and your household bills.',
'Switch to renewables':'Energy providers around the world are now offering greener tariffs. By switching to a company that provides electricity from solar, wind, or hydroelectric energy, you can reduce your household emissions and save money on your energy bills. You could even install solar panels if they`re readily available where you live. ',
'Buy energy efficient':'Electrical appliances are becoming more efficient by the year. What`s more, many countries now show how efficient particular products are, meaning you can make an informed choice. Whether it`s buying energy-saving light bulbs or choosing appliances with a high energy star rating, you can make your home more eco-friendly. Additionally, make sure to turn off and unplug anything you`re not using.',
'Use local food':'This is a tip that can apply to just about every area of life. Locally-grown produce takes less energy to transport and supports the economy where you live. If you can get your school to switch to local and sustainable food for the kitchen, you can help save the planet and help local businesses.',
'Fly direct':'The carbon footprint of flying is larger than any other mode of transport. While the Eurostar, for example, emits around 6g of CO2 per kilometre travelled, a domestic flight produces 133g of CO2 and 121g of other emissions.  When you do fly, you should aim to reduce the number of stops on your route, ideally by flying directly to your destination.',
'Offset your carbon':'Many airlines and travel companies now offer you the chance to offset your carbon emissions. Essentially, this is where you pay money on top of the cost of your ticket to fund projects aimed at reducing your carbon footprint. These carbon offsets cover all kinds of incentives, such as restoring forests and making energy and transportation more efficient.'
}

charities = {GREAT:('Cool Earth','Union of Concerned Scientists','Earth Justice', 'Earth Island'), 
MONEY:('Clean Air Task Force','Carbon180'), CHEAP:('Greenpeace','Earth Justice',
'Practical Action')}

charity_description = {'Cool Earth':'Fights to protect the earths rainforests, and help indigenous communities create sustainibility programs. You can donate to them directly or make purchases from their online shop to donate.',
'Union of Concerned Scientists':'A group that connects the scientific community with buisnesses to help reduce carbon emissions. You can donate to them through their website or you can help by becoming a member of the charity.',
'Clean Air Task Force':'A group that strongly advocates for the deployment of carbon capture technologies, in fact due to their current achievments they are aproximately saving 13,000 lives a year through reducing emissions. They can be donated to directly through their website.',
'Carbon180':'A charity that`s mostly focuses specifically on the research of carbon capture technologies, can be donated to directly through the website',
'Greenpeace':'Primarily investigates and exposes the main causes of damage to the environment, and has spent a considerable amount of time and energy in specifically protecting the artic ocean. They can be donated to through their website, but they also have ways to set up a fundraising event to donate and have petitions.',
'Earth Justice':'A group of lawyers dedicated to protecting the planet by handing out lawsuits and helping to pass laws that make the world more evironmentally freindly. They can be donated to through their website, additionally they offer many petitions to sign that help strengthen their cases.',
'Practical action': 'Works to help improve the livlihood of those in poorer communities by helping them start sustainability programs that are good for the community and the environment. They can be donated to throught their website, through the purchase of their wishlist items, or they offer you an option to set up a fundraiser.',
'Earth Island':'Offers support to start-up evironmental projects that serve to protect wildlife and fight climate change. In addition they serve to promote young leaders that want to make a change in the world. They can be donated to through their website, or if you have a well worked out environmental project proposal, they allow you apply for support from them.',
}

water = 'If you`re near a body of water see if there are any clean up organizations near you. Most water sources have become polluted and many cities have local programs that go out and clean trash out of the water. Additionally if you`re near a beach there`s bound to be a beach clean up program aswell' 