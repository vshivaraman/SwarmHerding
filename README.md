# SwarmHerding

This repo contains an implementation of the paper _Bio-Inspired Non-Cooperative Multi-Robot Herding_ by Alyssa Pierson and Mac Schwager.

The paper “Bio-inspired Non-cooperative Multi-Robot Herding” presents a new control strategy for a group of dog-like robots to drive a herd of non-cooperative sheep-like agents to a goal region in the environment. The sheep-like agents, which may be biological or robotic, respond to the presence of the dog-like robots with a repelling potential field common in biological models of the behavior of herding animals.

The key insight in designing control laws for the dog-like robots is to enforce geometrical relationships that allow for the combined dynamics of the dogs and sheep to be mapped to a simple unicycle robot model. The paper proves the convergence of a single sheep to a desired goal region using two or more dogs, and proposes a control strategy for the case of any number of sheep driven by two or more dogs.
