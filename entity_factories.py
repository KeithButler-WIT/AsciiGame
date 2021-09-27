#!/usr/bin/env python3

from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(63, 127, 63), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True)
cat = Entity(char="c", color=(255, 255, 255), name="Cat", blocks_movement=True)
dog = Entity(char="d", color=(255, 255, 255), name="Dog", blocks_movement=True)
sam = Entity(char="s", color=(255, 255, 255), name="Sam", blocks_movement=True)
badger = Entity(char="b", color=(50, 0, 0), name="Badger", blocks_movement=True)
