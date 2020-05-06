# Singleton

- DB repository
- Object factory
- Expensive initialization, once & accessible
- One copy
- Lazy initialization

## Singleton Allocator

Forcing allocation to return itself but shows initializer, so it compares if same type

## Singleton Decorator

Decorator allows to return object from instances

## Singleton Metaclass

Mix of the previous 2, helper `Singleton` forces allocation to return itself by `call` to return object from instances 

## Singleton Mono State

Create static object that anyone can call using a dictionary
Base class approach
Better use Decorator or Metaclass

## Singleton Testability

Always test implementations

## Summary

Laziness is easy, just init on first request
