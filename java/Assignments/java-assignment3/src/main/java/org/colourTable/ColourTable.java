package org.colourTable;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a table of RGB colors with a fixed capacity.
 * This class allows adding RGB colors while ensuring the number
 * of colors does not exceed the specified capacity and that RGB values
 * are within the valid range of 0-255.
 * <p>
 * Each color is stored as an array of three integers representing the
 * red, green, and blue components.
 */
public class ColourTable {
    private int size;
    private List<int[]> colours;

    /**
     * Constructs a ColourTable with the specified size.
     *
     * @param size The number of colors in the palette; must be a power of two and greater than 1.
     * @throws IllegalArgumentException if the size is not a valid power of two or is less than 2.
     */
    public ColourTable(int size) {
        if (size < 2 || (size & (size - 1)) != 0) {
            throw new IllegalArgumentException("Size must be a power of two and greater than 1");
        }
        this.size = size;
        this.colours = new ArrayList<>(); // Initialize the list
    }

    /**
     * Adds an RGB color to the color table.
     *
     * @param r The red component of the color (0-255).
     * @param g The green component of the color (0-255).
     * @param b The blue component of the color (0-255).
     * @throws IllegalArgumentException if any of the RGB components are out of the 0-255 range.
     * @throws IllegalStateException if the color table is already full.
     */
    public void add(int r, int g, int b) {
        if (colours.size() >= size) {
            throw new IllegalStateException("ColourTable is full");
        }

        if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255) {
            throw new IllegalArgumentException("Invalid RGB value: each component must be between 0 and 255");
        }

        colours.add(new int[]{r, g, b}); // Add the color as an int array
    }

    /**
     * Returns a copy of the list of RGB colors in the table.
     * This method ensures that the internal list is not modified
     * directly by external callers.
     *
     * @return A list of RGB color arrays, where each array contains three integers representing the red, green, and blue components.
     */
    public List<int[]> getColors() {
        return new ArrayList<>(colours); // Return a copy to avoid direct modification
    }
}
