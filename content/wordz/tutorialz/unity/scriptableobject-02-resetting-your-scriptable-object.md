Title: How To Reset Your ScriptableObject to a Default State
Date: 2022-02-20 10:20
status: hidden
Category: Wordz
Tags: tutorial, unity, unity-tutorial, scriptableobject
Slug: the-scriptable-object-what-why-and-how15
Authors: josh
Summary: Heard about all the ScriptableObject hype but still confused? Not sure how it can help you? This is your post!
showkofi: true

Link to earlier post in series

This post is part of a series. Want to see the earlier entries?

    - how to create a default state for an SO and set it back to its default state

Link to later post in series.

If you're following along with the series, you've created your first ScriptableObject.

You can grab the project from the last post here.

--

In the editor, ScriptableObjects can mutate. Look at our previous example.

With a limited number of ScriptableObjects, you can manually reset them, but as they grow this becomes tiring.

You can instantiate a copy of the ScriptableObject and only work with your copy.

Alternatively, you can _tell_ your ScriptableObject what its default state is.

## Enter... the default state.

## Not all ScriptableObjects need a default state.

## A more complicated example - a player inventory.

## Resetting on Editor Play

## Resetting With A Button

## Resetting Everything With A Button - The SO Manager
