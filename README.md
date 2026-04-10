<div align="center">
    <h2>Spark</h2>
    <p>by <a href= "https://github.com/HenryLi-0/spark"> @HenryLi-0 </a></p>
    <img src="frontimages/spark_banner.png" alt="banner"/>
</div>

<sub>All designs are open source! Hardware licensed under CERN OHL S v2.<sub>

---

## Spark

[Spark](https://github.com/HenryLi-0/spark) is an open source complex 3D printer, built for (and generously funded by) Hack Club's [Blueprint](https://blueprint.hackclub.com/)!

---

## What is this?

Following summer break, I realized I wasn't really doing much programming, CAD work, or pretty much anything significantly large. To simplify, I wanted to work on something to get out of creative limbo, something complex enough to grab my interest, and something that I would actually find myself using to create more.

With that said, along with 6 months of on and off work, I present my newest, top 1 hardest mechanical endurance design project, **Spark**. Compared to the mechanical design of [`Raven`](https://github.com/HenryLi-0/raven), Spark is significantly more complex, involving coreXY, belts, and bringing in the idea of a passive tool changer. (Note: In my opinion, one can't compare Spark and Raven, since they're both very complex in their own ways, Raven is more of an all-skill complexity, while Spark is more endurance and CAD.)

Spark uses [Klipper](https://www.klipper3d.org/), running on an SKR 1.4 Turbo Motherboard, to control its inputs. Powered through a Meanwell LRS-150-24, Spark features a coreXY motion system, which uses two NEMA17 42Ncm stepper motors. In this assembly, Spark is able to move the gantry, where a passive tool exchange system is utilized, using a latch, magnet, and guide system to align the tool head with the tool base. This allows Spark to use significantly less motors compared to a normal tool changer, using only one across all tools. With three motors down, Spark also has two more for Z control. In theory, this makes it capable of printing at a rotation, but that feature will probably be saved for a future date. 

The name Spark, apart from being possible foreshadowing (please no), is also meant to be trying to spark motivation to bounce back. Spark holds it difficulty in the lack of a fast reward function, meaning hours of CAD and research doesn't really translate directly to a "percent" or "progress". This, along with the mental struggles of pushing for time between an intense school year, really contributed to my personal rating of this journey. However, I don't regret my choice, and I feel the scope was fairly optimistic but achievable. In the end, Spark sorta achieved my initial personal goal, the one of trying to prove to myself that I was, infact, not washed and still capable of producing advanced projects. If anything its got the ball rolling again, and I definitely learned a lot more about the deep design behind FDM 3D printing. Well, that's it for now! Enjoy the showcase!

---

## Pictures!

![](</frontimages/assembly-2026-3-31.png>)

![](</frontimages/tool-area-2026-3-31.png>)

![](</frontimages/assembly-close-up-2026-3-31.png>)

![](</frontimages/wiring.png>)

---

## Directory

- [CAD](</CAD/README.md>)
    - Made in Onshape! Unlike last time, there's way too many print files to keep exporting them individually, so please check the CAD! 
- [Firmware](</firmware/README.md>)
    - We'll be using Klipper for this! Check out that folder for more info!
- [Updatelogs](</updatelogs/>)
    - Want to learn about the research and process behind stuff? Or want a REALLY long read? Check out the updatelogs! (It's WAY more extensive and detailed than on the Blueprint site!)
- [BOM](</BOM.csv>)
    - Want to build it yourself? Here's the BOM in CSV form! I suggest checking out the Google Sheets instead though, check down below for that!

---

## How to Use

Now, I don't exactly recommend trying to build this yet (as of 3/31/2026), but here we go:

**Assembly**

1. Get to the BOM and get shopping. You might need to find alternatives depending on where you are, and the price may be higher, given current global situations.
2. Firstly, pull up the CAD and get familiar with it. Don't use the `.STEP` file on this repository, the Onshape link is easier to use (and more updated)! Use logic to determine the order of steps, pay special attention to the extrusions and sliding in the T nuts, along with where wires would go.
3. There are no custom PCBs this time! Use the wiring diagram above to wire things up. PLEASE BE CAREFUL. Use common sense when dealing with power here. (Triple check this, along with the wiring diagram itself, and research this. Check with your local rules/regulations for more wiring size requirements!)
4. Back to CAD, assemble the main structure first, the tool base and coreXY seperately, then carefully attach the two segments. The tool base has been designed to be highly replaceable, but it is very deep inside the stack, so a lot of disassembly is required to safely remove parts. (Use the CAD!!!)
5. Ok, firmware time! Use Klipper docs and the wonderful resource of the internets to configure things! Some basic things to do are flashing a card for the main board, flashing a card for the pi, and changing the config file (research this!).

**Testing**

1. Great! Looks good? CHECK YOUR WIRING AGAIN!!! (Triple check it again, frying components is not fun!)
2. Nice, have a fire extinguisher on hand (or do this far from anything flammable), secure all components (including wires), and 
3. Safely test! Wear appropriate safety equipment and plug it in! Ideally, nothing explodes. If so, great! Make sure all components are properly powered, then feel free to work on adjusting the config file! Remember there is a switch to power off, along with pulling the plug, if safety ever requires it.
4. Once configs looks good, it's time for the first print! Check that coreXY actually moves (a straight line and a circle test are good first runs), along with the Z axis (check it reaches the top!). Also, ensure heated elements actually reach their goals (check thermistors but an external measurement would also be nice)! Once that's done, run a single color print!
5. Once that's all tuned, record some macros and work on getting tool changing to work! It might also be a good idea to test each tool beforehand!

---

## BOM

Note: This list was made in late March 2026. Depending on global situations, this price may change over time, so please be aware that prices in whatever future occurs may be different! Currently, shipping and tax estimates are included, but if you want to see the actual cost over time, check out `updatelogs` during construction time!

*Try using AliExpress Deals (Welcome Deal, along with deals every other day) on the stepper motors, as it's the most expensive component (you might need to order it by itself for the deal to only apply there, do research). The BOM uses the current deal on the stepper motors.*

Additionally, [here's](https://docs.google.com/spreadsheets/d/1Kiavj4VHOEFxnAxZlPTYNFeEL1XEMzFvvFbyFuPWtZs/) the original Google Sheets BOM, before it was compressed to this list. Reference that for a cleaner checklist!

|   Part                                            |   Price   | Link  |
|---------------------------------------------------|-----------|-------|
|   2020 Aluminum Extrusions (4pcs, 1220mm, Silver) |   $41.00 	| [Amazon](https://www.amazon.com/Aluminum-Extrusion-European-Standard-Anodized/dp/B0CLGX27MY/)
|   M3 10mm (8x40pcs)                               |   $12.16 	| [AliExpress](https://www.aliexpress.us/item/3256804341271555.html)
|   M3 14mm (2x40pcs)                               |   $3.22	| [AliExpress](https://www.aliexpress.us/item/3256804341271555.html)
|   M3 30mm (1x40pcs)                               |   $2.21	| [AliExpress](https://www.aliexpress.us/item/3256804341271555.html)
|   M3 2020 (3x100pcs)                              |   $20.31 	| [AliExpress](https://www.aliexpress.us/item/3256807638725964.html)
|   Motion Rods (2pc, 1000mm, 12mm)                 |   $30.00 	| [Amazon](https://www.amazon.com/12mm-350mm-13-78-inches-Vigorous-Hardened/dp/B0D4VQJN4F/)
|   NEMA 17 38mm Stepper Motor (5pcs)               |   $39.95 	| [AliExpress](https://www.aliexpress.us/item/3256808837281579.html)
|   GT2 Timing Pulley (with Shaft Collar)           |   $2.72 	| [AliExpress](https://www.aliexpress.us/item/3256808347934917.html)
|   T8 Lead Screw With Nut (200mm)                  |   $7.76 	| [AliExpress](https://www.aliexpress.us/item/3256807271104483.html)
|   T8 Lead Screw Motor Coupler (2pcs, D20L25)      |   $3.55 	| [AliExpress](https://www.aliexpress.us/item/2255799990666860.html)
|   623 Bearings (3x10pcs, 3x10x4mm)                |   $10.35 	| [AliExpress](https://www.aliexpress.us/item/3256807482131308.html)
|   GT2 Timing Belt (5m, W 6mm)                     |   $5.45 	| [AliExpress](https://www.aliexpress.us/item/3256803076577178.html)
|   LM12UU Linear Bearings (8pcs, LM12UU)           |   $8.65 	| [AliExpress](https://www.aliexpress.us/item/3256807105962945.html)
|   Magnets (50pcs, 4x2)                            |   $5.84 	| [AliExpress](https://www.aliexpress.us/item/3256810045272763.html)
|   TriangleLab V6 Volcano Hotend (3x1pcs, 24V)     |   $59.70 	| [AliExpress](https://www.aliexpress.us/item/2251832657765617.html)
|   Build Plate (MIC6/Aluminum)                     |   $0.00   | Anywhere
|   MeanWell USA LRS-150-24                         |   $18.40 	| [DigiKey](https://www.digikey.com/en/products/detail/mean-well-usa-inc/LRS-150-24/7705015)
|   IEC320 C14 Power Inlet                          |   $5.95	| [DigiKey](https://www.digikey.com/en/products/detail/adam-tech/IEC-GS-1-100/9831135)
|   250V 2.5A Fuse                                  |   $0.25	| [DigiKey](https://www.digikey.com/en/products/detail/littelfuse-inc/061702-5MXP/5233765)
|   C14 Power Wire						            |   $0.00   | Anywhere
|   LM2596 Buck Converter                           |   $3.22   | [AliExpress](https://www.aliexpress.us/item/3256807802058189.html)
|   Micro USB Cable to Power                        |   $0.00   | Anywhere
|   SKR 1.4 Turbo Motherboard                       |   $29.95 	| [Zyltech](https://www.zyltech.com/genuine-skr-1-4-turbo-3d-printer-control-board-by-bigtree-tech/)
|   A4988 Stepper Motor Controller (5pc, Red)       |   $5.41	| [AliExpress](https://www.aliexpress.us/item/3256808903461933.html)
|   Limit Switch (10pc, Pulley)                     |   $1.71 	| [AliExpress](https://www.aliexpress.us/item/3256805410237576.html)
|   Build Plate Heat Bed (100x100mm, 60W, 24V)      |   $27.74 	| [Keenovo](https://keenovo.store/products/keenovo-square-silicone-heater-3d-printer-build-plate-heatbed-heating-pad?variant=33194097803404)
|   Wires (16 AWG, 4m, 1 roll, Orange)              |   $4.53   | [AliExpress](https://www.aliexpress.us/item/3256807263561521.html)
|   SHIPPING: Shipping Price to NYC                 |   $6.99	| Amazon
|   ESTIMATED TAX                                   |   $6.92 	| Amazon
|   SHIPPING: Shipping Price to NYC                 |   $0.00	| AliExpress
|   SHIPPING: Shipping Price to NYC                 |   $5.00	| Zyltech
|   SHIPPING: Shipping Price to NYC                 |   $10.96 	| DigiKey
|   TOTAL                                           |   $379.90 | 
