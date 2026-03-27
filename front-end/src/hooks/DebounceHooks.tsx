import React from 'react';

interface DebounceProps {
    valueSearch: string;
    time: number;
}
export function useDebounce({ valueSearch, time }: DebounceProps) {
    const [debouncedValue, setDebouncedValue] = React.useState(valueSearch);
    React.useEffect(()=> {
        const timer = setTimeout(() => {
            setDebouncedValue(valueSearch);
        }, time);
        return () => clearTimeout(timer);
    }, [valueSearch, time])
    return debouncedValue;
}