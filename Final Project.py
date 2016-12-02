

while playing == True:
    if x pf is <= 0:   ##pf = player fuel
        playing == False:
    

## Interacting with the aliens
## Let x = the player
## Let cl = Civilization level
## Let al = Alien level
while gain_fuels == True:
    if cl < al:
        gain_fuels == False:
            current_fuel_level -= randint(1, current_fuel_level)
    if cl = al:
        gain_fuels == False:
            current_fuel_level -= randint(1, (current_fuel_level)/2)
    if cl > al:
        gain_fuels == True:
            current_fuel_level += radint(1, original_amount_fuel) ##original_amount_fuel = number of fuels in the plante
    
## Collecting Rocks in the planet
while collecting_rocks == True:
    if x is alive:
        collect_rocks = ((original_amount_rock)*1/3) ##original_amount_rock = number of the rocks in the plante
            original_amount_rock -= collcect_rocks   ##when you do this, you will change the amount of the rocks in the game board.
                                                     ##ALSO, this code should include the position of the number of the rocks in the plante, so that it changes to the changed value.
        
## Waiting to play for the next turn
while Waiting_next_turn == True:
    if x pf != 0:                    ## pf = player fuel
        Waiting_next_turn == True:
    else:
        Waiting_next_turn == False:
            return ("GAME OVER")
    
