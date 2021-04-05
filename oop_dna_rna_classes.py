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

    # case-sensitive to take into account alignment format with mixed case
    NUCLEOTIDES = 'T', 't', 'A', 'a', 'C', 'c', 'G', 'g', 'U', 'u'

    def __init__(self, sequence: str):
        if sequence and all(elem in self.NUCLEOTIDES for elem in sequence):
            self.sequence = sequence
        else:
            raise ValueError('Nucleic acid must contain only non-ambiguous nucleotides')

    def __len__(self):
        return len(self.sequence)

    # make object an iterable, not iterator
    def __iter__(self):
        return iter(self.sequence)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.sequence.upper() == other.sequence.upper()

    def __repr__(self):
        return f'NucleicAcid("{self.sequence}")'

    # for different hash values for NucleicAcid and string equal to
    # its sequence
    def __hash__(self):
        return hash((type(self), self.sequence))

    def gc_content(self):
        return sum(elem in ('G', 'g', 'C', 'c') for elem in self.sequence) / \
                self.__len__()


class Dna(NucleicAcid):

    COMPLEMENTS = dict(zip('AaTtCcGg', 'TtAaGgCc'))

    def __init__(self, sequence: str):
        super().__init__(sequence)
        if all(elem in self.NUCLEOTIDES[:-2] for elem in sequence):
            self.sequence = sequence
        else:
            raise ValueError('Dna sequence only consists of A C G T (a c g t) nucleotides')

    def __repr__(self):
        return f'Dna("{self.sequence}")'

    def reverse_complement(self):
        return type(self)(''.join((self.COMPLEMENTS[elem] for elem
                                   in reversed(self.sequence))))

    def transcribe(self):
        return Rna(''.join(('U' if elem == 'T' else 'u' if elem == 't' else elem for
                            elem in self.sequence)))


class Rna(NucleicAcid):

    COMPLEMENTS = dict(zip('AaUuCcGg', 'UuAaGgCc'))

    def __init__(self, sequence: str):
        super().__init__(sequence)
        if all(elem in self.NUCLEOTIDES[2:] for elem in sequence):
            self.sequence = sequence
        else:
            raise ValueError('Rna sequence only consists of A C G U (a c g u) nucleotides')

    def __repr__(self):
        return f'Rna("{self.sequence}")'

    def reverse_complement(self):
        return type(self)(''.join((self.COMPLEMENTS[elem] for elem
                                   in reversed(self.sequence))))
