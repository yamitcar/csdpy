from mamba import description, context, it
from expects import expect, equal

with description('Life') as self:
  with it('know the answer of everything?'):
    result = 42
    expect(result).to(equal(42))