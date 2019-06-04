import fresh_tomatoes
import media

the_host_2006=media.Movie("The Host","Careless American military personnel dump chemicals into South Korea's Han River.Several years later, a creature emerges from the tainted waters and sinks its ravenous jaws into local residents. When the creature abducts their daughter Ah-sung Ko,a vendor Song Kang-ho and his family decide that they are the only ones who can save her.","https://upload.wikimedia.org/wikipedia/en/5/55/The_Host_film_poster.jpg","https://www.youtube.com/watch?v=uoYURokHuZ4")

interstellar=media.Movie("Interstellar","In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist,is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper Matthew McConaughey and a team of researchers throughthe wormhole and across the galaxy to find out which of three planets could be mankind's new home.","https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg","https://www.youtube.com/watch?v=0vxOhd4qlnA")

kung_fu_hustle=media.Movie("Kung Fu Hustle","When the hapless Sing Stephen Chow and his dim-witted pal, Bone Feng Xiaogang, try to scam the residents of Pig Sty Alley into thinking they're members of the dreaded Axe Gang, the real gangsters descend on this Shanghai slum to restore their fearsome reputation. What gang leader Brother Sum (han Kwok-kwan doesn't know is that three legendary retired kung fu masters Yu Xing, Dong Zhihua, Chiu Chi-ling live anonymously in this decrepit neighborhood and don't take kindly to interlopers.","https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg","https://www.youtube.com/watch?v=-m3IB7N_PRk")

movies=(the_host_2006, interstellar, kung_fu_hustle)
fresh_tomatoes.open_movies_page(movies)
#the_host_2006.show_trailer()
