# Spellcraft

Repo contains spellcraft things

# Structure

* spellcraft - website
* docs - documentation and resources

# Models

* Type: code, name
* Resource: code, name
* Cost: spell, resource, quantity
* Spell: code, type, cost, summary, description, shortcut, rating

## Type

Type of spell

* code - meaningful key (A or AURA for Auras, ATK for Attacks)
* name - full name (Aura, Attack)

## Resource

### Description

Resources in the game

### Fields

* code - meaningful key (E for Earth, Y for Energy, W for Water)
* name - full name (Earth, Energy, Water)

## Cost

### Description

Cost of spell

### Fields

* spell - id of spell
* resource - id of resource
* quantity - amount of resource

### Example

Fireball requires three fires so
spell = "Fireball"
resource = "Fire"
quantity = "3"

## Spell

### Description

Spell entity

### Fields

* code
* type
* cost
* summary
* description
* shortcut
* rating

# Extras

* Comment: spell, title, description, user, timestamp
* Log: object, user, timestamp, event, activity

## Log

* object - id of object
* user - user who made change
* timestamp - time of change
* event - insert, update, delete
* activity - summary of change (field from x to y)

# Resources

* [960 Grid System](http://960.gs/)
* [How to add pinning](http://buildmypinnedsite.com/en-GB)