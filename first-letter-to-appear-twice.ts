function repeatedCharacter(s: string): string {
    let mySet = new Set<string>();
    for (const c of s){
        if (mySet.has(c))
            return c;
        else
            mySet.add(c);
    }
    return '';
};