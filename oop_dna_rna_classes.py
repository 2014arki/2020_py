#! usr/bin/env


# OOP (object oriented programing)
# Create Dna() and Rna() classes with next the properties:
# - are initialized with correspondent dna/rna string-sequence
# - evaluate GC-content with  gc_content method
# - create complement sequence with reverse_complement method
# - are iterable
# - instances with equal sequences must be equal (__eq__ method)
# - are hashable (can be added to the set)
# - instances of Dna-class can construct Rna-class instances with
# transcribe method


class NucleicAcid:

    NUCLEOTIDES = 'T', 'A', 'C', 'G', 'U'

    def __init__(self, sequence: str):
        if all(elem.upper() in self.NUCLEOTIDES for elem in sequence):
            self.sequence = sequence.upper()
            self.current_index = 0
        else:
            raise ValueError('Nucleic acid must contain only non-ambiguous DNA-nucleotides')

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.__len__():
            result = self.sequence[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(other, NucleicAcid):
            return self.sequence == other.sequence
        elif isinstance(other, type(self.sequence)):
            return self.sequence == other.upper()
        else:
            raise TypeError('Nucleic acid sequence comparable with only nucleotide sequence')

    def __hash__(self):
        return hash(self.sequence)

    def gc_content(self):
        return sum(elem in ('G', 'C') for elem in self.sequence) / self.__len__()


class Dna(NucleicAcid):
    COMPLEMENTS = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    def __init__(self, sequence: str):
        super().__init__(sequence)
        if all(elem in self.NUCLEOTIDES[:-1] for elem in sequence.upper()):
            self.sequence = sequence.upper()
        else:
            raise ValueError('Dna sequence only consists of A, C, G, T nucleotides')

    def reverse_complement(self):
        return type(self)(''.join((self.COMPLEMENTS[elem] for elem
                                   in reversed(self.sequence))))

    def transcribe(self):
        return Rna(''.join(('U' if elem == 'T' else elem for elem in self.sequence)))


class Rna(NucleicAcid):
    COMPLEMENTS = {
        'A': 'U',
        'U': 'A',
        'C': 'G',
        'G': 'C'
    }

    def __init__(self, sequence: str):
        super().__init__(sequence)
        if all(elem in self.NUCLEOTIDES[1:] for elem in sequence.upper()):
            self.sequence = sequence.upper()
        else:
            raise ValueError('Rna sequence only consists of A, C, G, U nucleotides')

    def reverse_complement(self):
        return type(self)(''.join((self.COMPLEMENTS[elem] for elem
                                   in reversed(self.sequence))))
