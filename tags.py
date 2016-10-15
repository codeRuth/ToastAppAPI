def tags(publisher):
	
	if publisher == "All Recipes":
		tag = '//span[@class="recipe-directions__list--item"]/text()'
	elif publisher == "Back to Her Roots":
		tag = '//li[@class="instruction"]/text()'
	elif publisher == "BBC Food":
		tag = '//p[@class="recipe-method__list-item-text"]/text()'
	elif publisher == "BBC Good Food":
		tag = ''
	elif publisher == "Bon Appetit":
		tag = '//div[@class="text" and @itemprop="recipeInstructions"]/text()'
	# elif (publisher == "Bunky Cooks"):  membership
	# 	tag = ''
	# elif (publisher == "Chow"):	json
	# 	tag = ''
	elif (publisher == "Closet Cooking"):
		tag = '//li[@itemprop="recipeInstructions"]/text()'
	elif (publisher == "Cookin Canuck"):
		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
	# elif (publisher == "Cookstr"): multiple travarsal
		#//div[@class="stepByStepInstructionsDiv" and @itemprop="recipeInstructions"/div[@class="sections"/div[@class="section"]/div[@class="cells"]/div[@class=""]/div[@class="articleAttrSection"]/text()


	#elif (publisher == "Delishhh"): uneven tagging
	#elif (publisher == "Eats Well With Others"): uneven tagging
		# //li[@class="instruction" and @itemprop="recipeInstructions"]/text()
	#elif (publisher == "Elana's Pantry"):	hyperlinking

	elif (publisher == "Epicurious"):
		tag = '//li[@class="preparation-step"]/text()'
	#elif (publisher == "Fine Dining Lovers"): multiple tags

	#elif (publisher == "Food Network"): hyperlinking

	elif (publisher == "Food Republic"):
		tag = '//span[@itemprop="recipeInstructions"]/ol/li/text()'
	elif (publisher == "Framed Cooks"):
		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
	elif (publisher == "Healthy Delicious"):
		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
	# elif (publisher == "Homesick Texan"): inconsistent
	elif (publisher == "Jamie Oliver"):
		tag = '//ol[@class="recipeSteps"]/li/text()'
	elif (publisher == "Lisa's Kitchen"):
		tag = '//li[@itemprop="recipeInstructions"]/p/text()'
	elif (publisher == "My Baking Addiction"):
	elif (publisher == "Panini Happy"):
	elif (publisher == "Pastry Affair"):
	elif (publisher == "PBS Food"):
	elif (publisher == "Picky Palate"):
	elif (publisher == "Pillsbury Baking"):
	elif (publisher == "Real Simple"):
	elif (publisher == "Serious Eats"):
	elif (publisher == "Smitten Kitchen"):
	elif (publisher == "The Pioneer Woman"):
	elif (publisher == "Two Peas and Their Pod"):
	elif (publisher == "Vintage Mixer"):
	elif (publisher == "What's Gaby Cooking"):
	

	else:
		return 404