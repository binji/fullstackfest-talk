#!/usr/bin/env python
import os
import sys

CODE = """\
i32.const 1
set_local $b
block $done
  loop $top
    get_local $n
    i32.const 0
    i32.le_s
    br_if $done
    get_local $a
    get_local $b
    tee_local $a
    i32.add
    set_local $b
    get_local $n
    i32.const 1
    i32.sub
    set_local $n
    br $top
  end
end
get_local $b
return"""
CODE_LINES = CODE.splitlines()

def MarkCode(line):
  lines = CODE_LINES[:]
  lines[line - 1] = '<mark>%s</mark>' % lines[line - 1]
  return '\n'.join(lines)

def MakeStack(stack):
  return ''.join('<box>%s</box>' % v for v in stack)

def MakeLocals(local):
  names = ['n', 'a', 'b']
  return ''.join('<box>$%s=%s</box>' % (names[i], v) for i, v in enumerate(local))

def Gen(mark_line, stack, local):
  return """\
        <section data-transition="none">
          <table>
            <tr><td>code</td><td>stack</td><td>locals</td></tr>
            <td>
          <pre><code data-noescape data-trim class="lisp no-max-height table-width">
%s
          </code></pre>
            </td>
            <td>%s</td>
            <td>%s</td>
          </table>
        </section>
""" % (MarkCode(mark_line), MakeStack(stack), MakeLocals(local))

lines = []
lines.append(Gen(1, [], [3, 0, 0]))
lines.append(Gen(2, [1], [3, 0, 0]))
lines.append(Gen(5, [], [3, 0, 1]))
lines.append(Gen(6, [3], [3, 0, 1]))
lines.append(Gen(7, [3, 0], [3, 0, 1]))
lines.append(Gen(8, [0], [3, 0, 1]))
lines.append(Gen(9, [], [3, 0, 1]))
lines.append(Gen(10, [0], [3, 0, 1]))
lines.append(Gen(11, [0, 1], [3, 0, 1]))
lines.append(Gen(12, [0, 1], [3, 1, 1]))
lines.append(Gen(13, [1], [3, 1, 1]))
lines.append(Gen(14, [], [3, 1, 1]))
lines.append(Gen(15, [3], [3, 1, 1]))
lines.append(Gen(16, [3, 1], [3, 1, 1]))
lines.append(Gen(17, [2], [3, 1, 1]))
lines.append(Gen(18, [], [2, 1, 1]))
lines.append(Gen(5, [], [2, 1, 1]))
lines.append(Gen(6, [2], [2, 1, 1]))
lines.append(Gen(7, [2, 0], [2, 1, 1]))
lines.append(Gen(8, [0], [2, 1, 1]))
lines.append(Gen(9, [], [2, 1, 1]))
lines.append(Gen(10, [1], [2, 1, 1]))
lines.append(Gen(11, [1, 1], [2, 1, 1]))
lines.append(Gen(12, [1, 1], [2, 1, 1]))
lines.append(Gen(13, [2], [2, 1, 1]))
lines.append(Gen(14, [], [2, 1, 2]))
lines.append(Gen(15, [2], [2, 1, 2]))
lines.append(Gen(16, [2 ,1], [2, 1, 2]))
lines.append(Gen(17, [1], [2, 1, 2]))
lines.append(Gen(18, [], [1, 1, 2]))
lines.append(Gen(5, [], [1, 1, 2]))
lines.append(Gen(6, [1], [1, 1, 2]))
lines.append(Gen(7, [1, 0], [1, 1, 2]))
lines.append(Gen(8, [0], [1, 1, 2]))
lines.append(Gen(9, [], [1, 1, 2]))
lines.append(Gen(10, [1], [1, 1, 2]))
lines.append(Gen(11, [1, 2], [1, 1, 2]))
lines.append(Gen(12, [1, 2], [1, 2, 2]))
lines.append(Gen(13, [3], [1, 2, 2]))
lines.append(Gen(14, [], [1, 2, 3]))
lines.append(Gen(15, [1], [1, 2, 3]))
lines.append(Gen(16, [1, 1], [1, 2, 3]))
lines.append(Gen(17, [0], [1, 2, 3]))
lines.append(Gen(18, [], [0, 2, 3]))
lines.append(Gen(5, [], [0, 2, 3]))
lines.append(Gen(6, [0], [0, 2, 3]))
lines.append(Gen(7, [0, 0], [0, 2, 3]))
lines.append(Gen(8, [1], [0, 2, 3]))
lines.append(Gen(21, [], [0, 2, 3]))
lines.append(Gen(22, [3], [0, 2, 3]))
print('\n'.join(lines))
