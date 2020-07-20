# foobar
## Tags
While they have removed option to check for `tags`, it is possible to request a challenge from any of these 
tags by writing `request <tag>`, e.g. `request algo`. 
```
foobar:~/ programmer$ tags
Requesting tags...
algo            algorithms
data_struct     data structures
low_level       low-level representation (binary representations, endianness)
math            math
crypto          security and cryptography
```

## Maven
Maven (see [`pom.xml`](pom.xml)) is used to build the solutions of these challenges.

Sample code to compile, run tests, run example code and remove the created files:
```bash
mvn compile
mvn test
(cd target/classes; java disorderly_escape.Solution)
mvn clean
```

## Tasks: round #1
### Level 1
* [`backward_and_forward`](tasks/backward_and_forward) time given: 48 hours

### Level 2
* [`zombit_infection`](tasks/zombit_infection) time given: 72 hours
* [`zombit_monitoring`](tasks/zombit_monitoring) time given: 72 hours

#### Notes
`zombit_infection` has a wrong 2nd test case in Foobar, check [StackOverflow](http://stackoverflow.com/questions/38006104/foobar-zombit-infection-challenge).

### Level 3
* [`when_it_rains_it_pours`](tasks/when_it_rains_it_pours) time given: 96 hours
* [`save_beta_rabbit`](tasks/save_beta_rabbit) time given: 96 hours
* [`spy_snippets`](tasks/spy_snippets) time given: 96 hours

### Level 4
* [`undercover_underground`](tasks/undercover_underground) time given: 144 hours
* [`minions_bored_game`](tasks/minions_bored_game) time given: 144 hours
* [`binary_bunnies`](tasks/binary_bunnies) time given: 144 hours
* [`breeding_like_rabbits`](tasks/breeding_like_rabbits) time given: 144 hours

### Level 5
* [`mad_science_quarterly`](tasks/mad_science_quarterly) time given: 192 hours
* [`grid_zero`](tasks/grid_zero) time given: 192 hours
* [`zombit_pandemic`](tasks/zombit_pandemic) time given: 192 hours
* [`dont_mind_the_map`](tasks/dont_mind_the_map) time given: 528 hours
* [`carrotland`](tasks/carrotland) time given: 360 hours

## Tasks: round #2
### Level 1
>Why did you sign up for infiltration duty again? The pamphlets from Bunny HQ promised exotic and interesting missions, yet here you are drudging in the lowest level of Commander Lambda's organization. Hopefully you get that promotion soon...

* [`solar_doomsday`](tasks/solar_doomsday) time given: 48 hours
> You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!

### Level 2
>The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator". You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying.

* [`lovely_lucky_lambs`](tasks/lovely_lucky_lambs) time given: 72 hours

>At least all this time spent running errands all over Commander Lambda's space station have given you a really good 
understanding of the station's layout. You'll need that when you're finally ready to destroy the LAMBCHOP and rescue the bunny prisoners.

* [`elevator_maintenance`](tasks/elevator_maintenance) time given: 72 hours

#### Notes
`elevator_maintenance` does not work with `Arrays.sort(T[] a, Comparator<? super T> c)`. So had to write my own 
MergeSort with a comparator.

>Awesome! Commander Lambda was so impressed by your efforts that she's made you her personal assistant. You'll be helping her directly with her work, which means you'll have access to all of her files-including the ones on the LAMBCHOP doomsday device. This is the chance you've been waiting for. Can you use your new access to finally topple Commander Lambda's evil empire?

>Who the heck puts clover and coffee creamer in their tea? Commander Lambda, apparently. When you signed up to infiltrate her organization, you didn't think you'd get such an up-close and personal look at her more...unusual tastes.

* [`bomb_baby`](tasks/bomb_baby) time given: 96 hours

>For a world-destroying despot with a penchant for making space-station-sized doomsday devices, Commander Lambda sure has good taste in office furniture. As her personal assistant, you have the latest in standing desk and ergonomic chair technology, and it sure makes a difference!

* [`doomsday_fuel`](tasks/doomsday_fuel) time given: 96 hours

>There are a lot of difficult things about being undercover as Commander Lambda's personal assistant, but you have to say, the personal spa and private hot cocoa bar are pretty awesome.

* [`find_the_access_codes`](tasks/find_the_access_codes) time given: 96 hours

>Excellent! You've destroyed Commander Lambda's doomsday device and saved Bunny Planet! But there's one small problem: the LAMBCHOP was a wool-y important part of her space station, and when you blew it up, you triggered a chain reaction that's tearing the station apart. Can you rescue the imprisoned bunnies and escape before the entire thing explodes?

### Level 4
>Six thousand, seven hundred and forty-one, six thousand, seven hundred and forty-two, six thousand, seven hundred and forty-three... Good grief! Just how many bunnies has Commander Lambda captured?!

* [`running_with_bunnies`](tasks/running_with_bunnies) time given: 360 hours

>Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

>It's a good thing bunnies are relatively small and light. You're pretty sure they're packing the escape pods well past the legal maximum occupancy.

* [`escape_pods`](tasks/escape_pods) time given: 360 hours

>Oh no! You escaped Commander Lambda's exploding space station - but so did she, and she's definitely not happy with you. She's chasing you in her heavily-armed starfighter, while you and your bunny refugees are stuck in these lumbering escape pods. It'll take all your wits and cleverness to escape such a hare-y situation, so you'd better hop to it!

### Level 5
> Uh-oh, your HUD shows half a dozen missiles headed your way. Better do a barrel roll!
* [`disorderly-escape`](tasks/disorderly-escape) time given: 528 hours

>With one last roar of the escape pod's engines, you and your bunny companions jump to lightspeed. Congratulations! You've destroyed the LAMBCHOP, rescued the bunnies, gotten Commander Lambda off your tail, and saved the galaxy. Time for a little rest and relaxation back on Bunny Planet. Pat yourself on the back - you've earned it!

```
<encrypted>
NUYeEE0vBAAHSUFXRWkGHwBPOEZfVEkCAgkiBAwCWylGU05ORggWOgQICEsoRl9USQQLAyETGRYJ bFtTUwcPDhcrBQQHQilGX1RJAA4NJwQbAEMpDwdTTltNQjsPAQpNJwQXU0JBShcvAw8MWj9GU05O Rh4EKARKSQ5rBxwbSUFXRWkWBAsPaxw=
</encrypted>
```

Decrypted by [`encrypted_message`](src/encrypted_message/Decrypt.java):
```
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
```

* [`dodge-the-lasers`](tasks/dodge-the-lasers) time given: 528 hours
